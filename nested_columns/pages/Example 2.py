import numpy as np
import pandas as pd
import streamlit as st
st.set_page_config(layout="wide")
import streamlit_nested_layout


"""
# Example 2
This is an early version of the app we built for Summit. I wanted to have the "Save" 
button next to the metric but couldn't do it back then. 

---
"""
st.write(
    "<style>[data-testid='stMetricLabel'] {display: none}</style>",
    unsafe_allow_html=True,
)
col1, col2 = st.columns(2, gap="large")
with col1:
    st.header("Budgets for July")
    st.caption("Assign budgets (in k$) to each of the channels below.")
    st.slider("Search engine", value=29)
    st.slider("Social media", value=18)
    st.slider("Email", value=68)
    st.slider("Video", value=72)

with col2:
    st.header("Predicted ROI")
    st.caption("Each time you update the widgets, the app runs a new prediction.")
    subcol1, subcol2 = st.columns(2)
    subcol1.metric("ROI", "$ 19.73 million", delta="0.0 % vs June")
    # subcol2.write("")
    subcol2.button("Save")
    st.write("")
    st.bar_chart(np.random.rand(100))

"""
---
Takeaways:
- It looks OK but this was probably not a good idea in the first place :D
- The "Save" button is not aligned with the metric. Again, this is the problem that
  text elements have some "padding" due to the line height, while the button doesn't 
  have any padding. Not sure how we'd solve that. st.space is one option but you'd 
  really move pixels around then. 
- On small screens, the metric gets cut off. That's not the intended behavior 
  specced out originally. It should ellipsize. Need to fix. 
- Horizontal container would probably be the better solution here, then the metric 
  could simply take the space it needs. 
- st.metric doesn't have label_visibility. That's a bug, we need to add it. 
- Anyway, all of this isn't a blocker for nested columns IMO. Just a) this isn't a 
  perfect use case and b) other stuff we should fix. 
"""
