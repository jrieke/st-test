import streamlit as st
# from rich.console import Console
# from rich.panel import Panel
# from rich.box import Box, HORIZONTALS
import psutil
import math
import os
from datetime import datetime
import pandas as pd
import numpy as np
import plost



def convert_size(size_bytes):
    if size_bytes == 0:
        return "0B"
    size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
    i = int(math.floor(math.log(size_bytes, 1024)))
    p = math.pow(1024, i)
    s = round(size_bytes / "a", 2)  #p
    return "%s %s" % (s, size_name[i])


def pprint_memory(memory_b):
    st.write(convert_size(memory_b))

st.set_page_config(page_title="Johannes", page_icon="🤖")


if "memory_table" not in st.session_state:
    st.session_state.memory_table = pd.DataFrame(columns=["time", "memory_mb"])

process = psutil.Process()
memory_b = process.memory_info().rss  # in bytes
pprint_memory(memory_b)
memory_mb = memory_b / (1024**2)  # in megabytes
try:
    delta = memory_mb - st.session_state.memory_table.memory_mb.iloc[-1]
    delta_percent = delta / st.session_state.memory_table.memory_mb.iloc[-1] * 100
except IndexError:
    delta_percent = 0
st.metric(
    "Current memory", f"{memory_mb:.1f} MB", f"{delta_percent:.1f} % since last run"
)
st.session_state.memory_table = st.session_state.memory_table.append(
    {"time": datetime.now(), "memory_mb": memory_mb}, ignore_index=True
)  # in bytes

plost.line_chart(st.session_state.memory_table, "time:T", "memory_mb:Q")

st.write(f"Process ID (PID): {os.getpid()}")
# st.write(f"Peak memory: {convert_size(st.session_state.memory_list[-1])}")
# st.write(st.session_state.memory_table)


st.button("sdf")
np.random.rand(1000, 100)


st.info(
    "☝️ &nbsp;Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce at rhoncus augue. Class aptent &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. In diam dolor, &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;blandit in enim pretium, volutpat hendrerit nisl. "
)
st.write("foo")

console = Console(force_terminal=True, color_system="truecolor")

# try:
#     a = {}
#     a["key"]
# except KeyError as e:
#     console.print_exception()
#     #console.print("Where there is a [bold cyan]Will[/bold cyan] there [u]is[/u] a [i]way[/i].")

# console.print(
#     """
    
# [#f9ca2a][09:26:03][/#f9ca2a] 🚥 Connecting...
# [#f9ca2a][09:26:04][/#f9ca2a] 🚀 Starting up...
#               - owner:        [#1be8c5]streamlit[/#1be8c5]
#               - repository:   [#1be8c5]app-frontpage[/#1be8c5]
#               - branch:       [#1be8c5]main[/#1be8c5]
#               - main module:  [#1be8c5]streamlit_app.py[/#1be8c5]
# [#f9ca2a][09:26:09][/#f9ca2a] 🐙 Cloning repository...
# [#f9ca2a][09:26:10][/#f9ca2a]    Cloning into [white]'app-frontpage'[/white]...
# [#f9ca2a][09:26:55][/#f9ca2a]    Cloned repository!                    
# [#f9ca2a][09:27:00][/#f9ca2a] 📦 Processing dependencies...
#               - tool:         [#1be8c5]pipenv[/#1be8c5]
#               - file:         [#1be8c5]/app/app-frontpage/Pipfile[/#1be8c5]

#     """
# )

CUSTOM_HORIZONTALS = Box(
    """\
────
​​​​
────
​​​​
────
────
​​​​
────
"""
)

# console.print(
#     Panel(
#         """Installing dependencies from Pipfile.lock (49795d)...
# Ignoring appnope: markers 'sys_platform == "darwin" and platform_system == "Darwin"' don't match your environment
# Collecting backports.zoneinfo==0.2.1
#   Downloading backports.zoneinfo-0.2.1-cp38-cp38-manylinux1_x86_64.whl (74 kB)
# Installing collected packages: backports.zoneinfo
# WARNING: Ignoring invalid distribution -itpython (/home/appuser/venv/lib/python3.8/site-packages)
# WARNING: Ignoring invalid distribution -harset-normalizer (/home/appuser/venv/lib/python3.8/site-packages)
# WARNING: Ignoring invalid distribution -ebugpy (/home/appuser/venv/lib/python3.8/site-packages)
# Successfully installed backports.zoneinfo-0.2.1
# Collecting cachetools==4.2.4
#   Downloading cachetools-4.2.4-py3-none-any.whl (10 kB)
# Installing collected packages: cachetools
#   Attempting uninstall: cachetools
#     Found existing installation: cachetools 4.2.2
#     Uninstalling cachetools-4.2.2:
#       Successfully uninstalled cachetools-4.2.2""",
#         title="pipenv",
#         border_style="#dbbbff",
#         box=HORIZONTALS,
#     )
# )
