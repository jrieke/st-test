import streamlit as st
import pandas as pd
import datetime


st.write("hello")

# Create a random dataframe.
data = {
    'text': ['apple', 'banana', 'cherry', 'date'],
    'number': [1, 2, 3, 4],
    'boolean': [True, False, True, False],
    'datetime': [datetime.datetime(2022, 1, 1),
                 datetime.datetime(2022, 1, 2),
                 datetime.datetime(2022, 1, 3),
                 datetime.datetime(2022, 1, 4)]
}

df = data#pd.DataFrame(data)
df = {"a": 1, "b": 2} 
st.experimental_data_editor


st.experimental_data_editor(df)#, num_rows="dynamic", use_container_width=True)#, num_rows="dynamic", key="data")
#st.session_state.data