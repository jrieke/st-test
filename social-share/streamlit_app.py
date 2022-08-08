import asyncio
import time

from PIL import Image, ImageOps
import pyppeteer
import streamlit as st
import numpy as np


st.write(
        f'<span style="font-size: 78px; line-height: 1">🌸</span>',
        unsafe_allow_html=True,
    )
"""
# Social share demo

Enter an app URL and see what its social share image would look like. 
"""


async def _save_screenshot(
    url: str, img_path: str, sleep: int = 5, width: int = 1024, height: int = 576
) -> None:
    browser = await pyppeteer.launch(handleSIGINT=False, handleSIGTERM=False, handleSIGHUP=False)
    page = await browser.newPage()
    await page.goto(url, {"timeout": 6000})  # increase timeout to 60 s for heroku apps
    await page.emulate({"viewport": {"width": width, "height": height}})
    time.sleep(sleep)
    # Type (PNG or JPEG) will be inferred from file ending.
    await page.screenshot({"path": img_path})
    await browser.close()
    

@st.experimental_memo(ttl=24*3600)
def take_screenshot(url, sleep, width, height, trim_top):
    # Take screenshot at increased height, then cut off bottom, so we get rid of the red 
    # Streamlit logo in the bottom right. 
    increased_height = 1.2 * height + trim_top
    # TODO: Should create temp file here instead. 
    # Attach ?embed=true to the url to get rid of the chrome at the top and hamburger menu.
    asyncio.run(_save_screenshot(url + "?embed=true", "screenshots/test.png", sleep=sleep, width=int(width), height=int(increased_height)))
    screenshot = Image.open("screenshots/test.png")
    screenshot = screenshot.crop((0, trim_top, width, height+trim_top))
    screenshot = screenshot.resize((1024, 572))
    return screenshot

# def trim(im):
#     # https://stackoverflow.com/questions/9396312/use-python-pil-or-similar-to-shrink-whitespace
#     pix = np.asarray(im)
#     pix = pix[:,:,0:3] # Drop the alpha channel
#     idx = np.where(pix-255)[0:2] # Drop the color when finding edges
#     box = list(map(min,idx))[::-1] + list(map(max,idx))[::-1]
#     region = im.crop(box)
#     return region
    
url = st.text_input("App URL")
col1, col2, col3, col4 = st.columns(4)
sleep = col1.number_input("Wait after page load (s)", 0, 60, 5, help="A Streamlit app always takes a few seconds to load properly. This is the amount of time to wait after the page has loaded before taking a screenshot.")
width = col2.number_input("Screenshot width", 1, 3000, 1300, help="Decrease this if you want to have less whitespace on the left and right side of the screenshot.")
height = col3.number_input("Screenshot height", 1, 3000, int(width/1024*572), disabled=True)
trim_top = col4.number_input("Trim at top", 0, 1000, 0, help="This is the amount of pixels to trim off the top of the screenshot. Increase to reduce the whitespace at the top of the page.")
# do_trim = st.checkbox("Trim whitespace")

    
if url:
    st.write("")
    screenshot = take_screenshot(url, sleep, width, height, trim_top)
    st.write("##### Here's the screenshot:")
    st.caption("If you see nothing, increase the wait time above.")
    st.image(screenshot, use_column_width=True)
    
    st.write("")
    st.write("##### And here's the social share image:")
    template = Image.open("template.png")
    combined = template.copy()
    combined.paste(screenshot, (92, 126))
    st.image(combined)
    