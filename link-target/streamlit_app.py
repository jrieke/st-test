import streamlit as st

"## The streamlit repo"
st.markdown(
    '<a href="https://github.com/streamlit/streamlit">default</a>',
    unsafe_allow_html=True,
)
st.markdown(
    '<a href="https://github.com/streamlit/streamlit" target="_blank">blank</a>',
    unsafe_allow_html=True,
)
st.markdown(
    '<a href="https://github.com/streamlit/streamlit" target="_self">self</a>',
    unsafe_allow_html=True,
)
st.markdown(
    '<a href="https://github.com/streamlit/streamlit" target="_parent">parent</a>',
    unsafe_allow_html=True,
)
st.markdown(
    '<a href="https://github.com/streamlit/streamlit" target="_top">top</a>',
    unsafe_allow_html=True,
)

"## Page 2"
st.markdown(
    '<a href="/page2">default</a>',
    unsafe_allow_html=True,
)
st.markdown(
    '<a href="/page2" target="_blank">blank</a>',
    unsafe_allow_html=True,
)
st.markdown(
    '<a href="/page2" target="_self">self</a>',
    unsafe_allow_html=True,
)
st.markdown(
    '<a href="/page2" target="_parent">parent</a>',
    unsafe_allow_html=True,
)
st.markdown(
    '<a href="/page2" target="_top">top</a>',
    unsafe_allow_html=True,
)
