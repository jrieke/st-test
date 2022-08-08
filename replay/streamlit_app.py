import streamlit as st
import time

import pandas as pd
import numpy as np
np.random.seed(0)
df = pd.DataFrame(np.random.randn(100, 4), columns=list('ABCD'))

@st.experimental_memo(suppress_st_warning=True)
def add_df(i):
    time.sleep(1)
    st.line_chart(df + i)
    slider = st.slider("sdfsd")
    st.write(slider)
    
    
i = st.number_input("number", 1, 10, 1)
add_df(i)

st.sidebar.write("hello")