import time

import streamlit as st

if "last_cache_duration" not in st.session_state:
    st.session_state["last_cache_duration"] = 5

@st.cache
def square(n):
    time.sleep(3)
    return n**2


start_time = time.time()
n = st.slider("Number", 1, 10)
square(n)
duration = time.time() - start_time
"The result is:", square(n)
st.caption(f"Took {duration:.2f} seconds")
