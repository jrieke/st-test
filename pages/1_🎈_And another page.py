import streamlit as st


if st.experimental_user.email in ["johannes.rieke@streamlit.io", "test@localhost.com"]:
    st.write(f"Hey there {st.experimental_user.email}, here are some balloons for you!")
    st.balloons()
else:
    st.error("✋ This page is only for cool kids.")

