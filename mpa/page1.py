import streamlit as st

st.write("This is page 1")

st.markdown('<a href="/page2" target="_self">Go to page 2</a>', unsafe_allow_html=True)

st.selectbox("foo", ["bar", "baz"], -1)