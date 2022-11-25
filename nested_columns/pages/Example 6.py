import numpy as np
import pandas as pd
import streamlit as st
import streamlit_nested_layout

"""
# Example 6
https://discuss.streamlit.io/t/column-layout/28937

---
"""

col1, col2 = st.columns(2, gap="large")
with col1:
    subcol1, subcol2 = st.columns(2, gap="medium")
    subcol1.write(
        "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. "
    )
    subcol2.write(
        "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. "
    )
    st.write("")
    st.write(
        "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book."
    )

with col2:
    subcol1, subcol2 = st.columns(2, gap="medium")
    subcol1.write(
        "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type."
    )
    subcol2.write(
        "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type."
    )

    st.write("")
    subcol1, subcol2 = st.columns(2, gap="medium")
    subcol1.write(
        "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type."
    )
    subcol2.write(
        "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type."
    )


# Takeaways:
# - Looks great!