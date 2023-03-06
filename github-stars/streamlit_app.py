import asyncio
import re
import time

import aiohttp
import gui
import pandas as pd
import requests
import streamlit as st
from rich import print
from streamlit_tags import st_tags

gui.icon("⭐️")
"# Github stars"

HEADERS = {
    "Accept": "application/vnd.github.v3.star+json",
    "Authorization": f"token {st.secrets.gh_token}",
}


def flatten(l):
    return [item for sublist in l for item in sublist]


def check_response(response):
    try:
        status = response.status  # aiohttp
    except AttributeError:
        status = response.status_code  # requests
    if status != 200:
        st.error(
            f"Crawling Github failed with status code {status}. This is *probably* due "
            "to a rate limit on the Github API. Please wait ~1 hour for the limit to "
            "reset or check the logs for more detail.",
            icon="🐌",
        )
        st.stop()


async def get_stars_from_page(session, repo, page):

    url = f"https://api.github.com/repos/{repo}/stargazers?per_page=30&page={page}"
    async with session.get(url) as response:
        check_response(response)
        stargazers = await response.json()

        # Print info on rate limits.
        limit = response.headers["X-RateLimit-Limit"]
        used = response.headers["X-RateLimit-Used"]
        remaining = response.headers["X-RateLimit-Remaining"]
        print(
            f"Crawling page {page} -> status {response.status} (remaining API requests: "
            f"{remaining}, limit: {limit}, used: {used})"
        )

        return [s["starred_at"] for s in stargazers]


async def _get_all_stars(repo):
    print(f"Crawling stars for '{repo}'...")

    # Get number of pages. This can be done without async, as we need to wait for the
    # result anyway, so just using requests here.
    response = requests.get(
        f"https://api.github.com/repos/{repo}/stargazers?per_page=30", headers=HEADERS
    )
    check_response(response)
    match = re.search("next.*&page=(\d*).*last", response.headers["Link"])
    last_page = int(match.group(1))
    print("Last page is:", last_page)

    # just for debugging
    # last_page = 5

    start_time = time.time()
    async with aiohttp.ClientSession(headers=HEADERS) as session:
        # Process all pages simultaneously, via asyncio + aiohttp.
        tasks = [
            get_stars_from_page(session, repo, page) for page in range(1, last_page + 1)
        ]
        all_stars = await asyncio.gather(*tasks)

    all_stars = flatten(all_stars)
    print(f"Found stars:", len(all_stars))
    print(f"--- {time.time() - start_time:.3f} seconds ---")
    print()
    return all_stars


@st.experimental_memo(ttl=48 * 3600)
def get_all_stars(repo):
    return asyncio.run(_get_all_stars(repo))


repos = st_tags(
    label="Repos to visualize",
    text="owner/repo (then press enter)",
    value=[
        "streamlit/streamlit",
        "gradio-app/gradio",
        "plotly/dash",
        "voila-dashboards/voila",
        "holoviz/panel",
    ],
)

if repos:
    dfs = []

    for repo in repos:
        # Crawl starred_at datetimes for this repo and convert to dataframe.
        all_stars = get_all_stars(repo)
        df_all_stars = pd.DataFrame(all_stars, columns=["starred_at"])

        # Get rid of time, keep only date.
        df_all_stars = pd.to_datetime(df_all_stars["starred_at"]).dt.date

        # Count how many stars there are for each date.
        df_counts = df_all_stars.value_counts(sort=False).rename(repo)

        dfs.append(df_counts)

    # Merge the dataframes for all repos into one.
    df_new_stars = pd.concat(dfs, axis=1).fillna(0).astype(int).sort_index()
    df_total_stars = df_new_stars.cumsum()

    # Show charts.
    gui.colored_header("Star count over time")
    st.line_chart(df_total_stars)

    gui.colored_header("New stars per day")
    avg = st.checkbox("Rolling average (28 days)", True)
    if avg:
        df_new_stars = df_new_stars.rolling(28).mean()
    st.line_chart(df_new_stars)
