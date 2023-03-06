import streamlit as st

"""
# My new app

This is a demo for...
"""

with open("3d.html", "r") as f:
    st.components.v1.html(f.read(), height=400)
