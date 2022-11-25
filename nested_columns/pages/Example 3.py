import numpy as np
import pandas as pd
import streamlit as st
import streamlit_nested_layout

"""
# Example 3
https://discuss.streamlit.io/t/columns-in-a-column/21978

Note that the exact case from the post could be solved without nested columns. But you'd need it if you want to have any variation between the widths of the elements. 

---
"""

col1, col2 = st.columns(2, gap="medium")

subcol1, subcol2 = col1.columns([1, 2])
subcol1.metric("A metric", 123456, 123)
subcol2.line_chart(np.random.rand(10), height=200)

subcol1, subcol2 = col1.columns([1, 2])
subcol1.metric("A metric", 123456, 123)
subcol2.line_chart(np.random.rand(10), height=200)

subcol1, subcol2 = col1.columns([1, 2])
subcol1.metric("A metric", 123456, 123)
subcol2.line_chart(np.random.rand(10), height=200)

col2.write(
    "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."
)
col2.write(
    "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."
)

# Takeaways:
# - Again, metrics are getting cut off while they should be ellipsized. 
# - Otherwise looks good. But of course doesn't really need nested columns...