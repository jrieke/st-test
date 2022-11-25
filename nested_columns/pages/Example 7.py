import numpy as np
import pandas as pd
import streamlit as st

st.set_page_config(layout="wide", initial_sidebar_state="collapsed")
import streamlit_nested_layout

"""
# Example 7
https://discuss.streamlit.io/t/support-for-nested-columns/28810

This is a super complex layout. It requires 2 levels of nesting and I even left out 
a few details of the original request. We shouldn't support this!

---
"""
left_banner, main_area = st.columns([0.05, 0.95])
with left_banner:
    st.write("⚒️")
    st.write("❌")
    st.write("♻️")
    st.write("🗑️")
    st.write("🔌")
    st.write("⬇️")
    st.write("🔊")
    st.write("🎥")
    st.write("🌍")
    st.write("ℹ️")
with main_area:
    st.info("Some banner at the top of the page", icon="📣")
    col1, col2, col3 = st.columns([3, 3, 1], gap="medium")
    with col1:
        st.line_chart(np.random.rand(10))
        subcol1, subcol2 = st.columns([1, 5])
        subcol1.write(
            "Lorem Ipsum is simply dummy text of the printing and typesetting industry. "
        )
        subcol2.dataframe(np.random.rand(10, 10), use_container_width=True, height=150)
        subcol2.dataframe(np.random.rand(10, 10), use_container_width=True, height=150)

    with col2:
        st.bar_chart(np.random.rand(10))
        st.dataframe(np.random.rand(10, 10), use_container_width=True, height=250)
        st.write(
            "Lorem Ipsum is simply dummy text of the printing and typesetting industry. "
        )
        st.write("Lorem Ipsum is simply dummy text. ")

    with col3:
        st.image(
            "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTtBb-bopcInKq0ITjKnJe8t_vnt6PpO095gvhRht2pVQ&s",
            use_column_width=True,
        )
        st.image(
            "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTtBb-bopcInKq0ITjKnJe8t_vnt6PpO095gvhRht2pVQ&s",
            use_column_width=True,
        )
        st.image(
            "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTtBb-bopcInKq0ITjKnJe8t_vnt6PpO095gvhRht2pVQ&s",
            use_column_width=True,
        )
        st.image(
            "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTtBb-bopcInKq0ITjKnJe8t_vnt6PpO095gvhRht2pVQ&s",
            use_column_width=True,
        )
        st.image(
            "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTtBb-bopcInKq0ITjKnJe8t_vnt6PpO095gvhRht2pVQ&s",
            use_column_width=True,
        )


# Takeaways
# - Yeah, this is way too complex for a Streamlit app.
# - Side note: dataframe doesn't resize if sidebar is collapsed, we should fix that (with use_container_width=True).
# - It also looks weird on small screen sizes. Because there are so many columns,
#   they naturally become very small. So if you make the window small, they become tiny,
#   which makes things look weird. E.g the text in the top left gets stretched out vertically way too much.
#   And the images on the right side don't have the same height as the rest of the content any more.
# - On mobile it's OK actually since everything is just below each other. The toolbar on the
#   left looks weird but OK, can't really change that much.
