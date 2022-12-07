import numpy as np
import pandas as pd
import streamlit as st
import streamlit_nested_layout

"""
# Example 5
https://discuss.streamlit.io/t/specific-layout-without-nested-columns/22861

---
"""
col1, col2 = st.columns([1, 2], gap="medium")
with col1:
    "## Header text"
    st.line_chart(np.random.rand(10), height=250)
    st.line_chart(np.random.rand(10), height=250)

with col2:
    "## More header text"
    with st.expander("Show charts", expanded=True):
        subcol1, subcol2 = st.columns(2)
        subcol1.line_chart(np.random.rand(10), height=250)
        subcol2.line_chart(np.random.rand(10), height=250)
    st.expander("Show dataframe").dataframe(
        np.random.rand(10, 10), use_container_width=True, height=250
    )

    "## More header text"
    with st.expander("Show charts"):
        subcol1, subcol2 = st.columns(2)
        subcol1.line_chart(np.random.rand(10), height=250)
        subcol2.line_chart(np.random.rand(10), height=250)

"""
---
Takeaways:
- Looks good. Expanders thing is a bit weird but OK. 
- Especially like it with gap="medium" here! I think gap makes nested columns look so 
  much better in many situations because you get more visual separation. 
"""
