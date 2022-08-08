import streamlit as st
from vega_datasets import data

source = data.seattle_weather()
source

st.area_chart(source, x="date", y=["temp_min", "temp_max"])
st.write("hello123456")

