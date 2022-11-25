import numpy as np
import pandas as pd
import streamlit as st
import streamlit_nested_layout

"""
# Example 1
Complex widget layout on one side, chart/image/map on the other side. That's the top use case that's always brought up. 

---
"""

# with st.sidebar:
col1, col2 = st.columns(2, gap="medium")
# col1.write("## Column 1")
# col2.write("## Column 2")

right_side = col1.radio("Show on right side 👉", ["Chart", "Image", "Map"], horizontal=True)
# right_side = "Chart"
subcol1, subcol2 = col1.columns(2)
subcol1.text_input("Text input 1")
subcol2.text_input("Text input 2")
# subcol3.text_input("Text input 3")
# subcol4.text_input("Text input 4")
col1.text_area("Text Area 1")
# col1.radio("Options", ["One", "Two", "Three", "Four", "Five"], horizontal=True)
subcol1, subcol2, subcol3, subcol4 = col1.columns(4)
subcol1.checkbox("One")
subcol2.checkbox("Two")
subcol3.checkbox("Three")
subcol4.checkbox("Four")

if right_side == "Chart":
    # TODO: Theme doesn't work here. Is that a bug??
    col2.bar_chart(np.random.rand(100))
elif right_side == "Image":
    col2.image(
        "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTtBb-bopcInKq0ITjKnJe8t_vnt6PpO095gvhRht2pVQ&s",
        use_column_width=True,
    )
elif right_side == "Map":
    df = pd.DataFrame(
        np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4], columns=["lat", "lon"]
    )
    col2.map(df)
else:
    raise ValueError(f"Unexpected right_side: {right_side}")



# Takeaways:
# - Looks good
# - Checkbox wraps weirdly but that's because there's an unnecessary padding on the right side. We should jut remove that, and then we should be good. 
# - Padding above chart and image should be a bit increased but that's unrelated to nested columns. Map e.g. has a good top padding. 