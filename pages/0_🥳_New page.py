import streamlit as st
import numpy as np

st.title("New page")

import seaborn as sns

iris = sns.load_dataset('iris')
iris["bool"] = np.random.choice([True, False], len(iris))
st.dataframe(iris)
