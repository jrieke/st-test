import streamlit as st
import time

text = st.text_input("Enter some text", live=True)
st.write(text)