import numpy as np
import pandas as pd
import streamlit as st
import streamlit_nested_layout
import os

"""
# Example 4
https://discuss.streamlit.io/t/need-help-with-layout-columns-within-columns/12912

---
"""

if os.path.exists("vertical_banner.jpg"):
    img = "vertical_banner.jpg"
else:
    img = "nested_columns/vertical_banner.jpg"

col1, col2 = st.columns([1, 3], gap="medium")
col1.write("")
col1.image(img, use_column_width=True)

with col2:
    "# This is a title"
    subcol1, subcol2, subcol3 = st.columns(3)
    subcol1.multiselect("Select something", ["Option 1", "Option 2", "Option 3"])
    subcol2.multiselect("Select something 2", ["Option 1", "Option 2", "Option 3"])
    subcol3.multiselect("Select something 3", ["Option 1", "Option 2", "Option 3"])
    st.write("")
    st.dataframe(np.random.rand(10, 10), use_container_width=True)


# Takeaways:
# - Looks good
# - "Choose an option" in multiselect is moved to the next line if it's too small. We 
#   should fix that. 