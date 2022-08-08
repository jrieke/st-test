import streamlit_patches as st

def home():
    st.icon("👩‍💻")
    st.title("Homepage")
    
st.page(home, "Homepage", "👩‍💻")
st.page("apps/page1.py", "Page 1", "🌸")

from apps.page1 import __title__
