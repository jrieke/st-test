import numpy as np
import streamlit as st
import streamlit_hacks

start = st.slider("Start array at...")
arr = np.arange(start, 10000 + start, 1)


# With st.cache -----------------------------------------------------
# @st.cache
# def square(arr):
#     return arr * arr

# squared_arr = square(arr)

# # This throws CachedObjectMutationWarning with st.cache, since we are modifying the
# # cached object.
# squared_arr[0] = -1

# col1, col2 = st.columns(2)
# with col1:
#     st.write("Original")
#     st.dataframe(arr)
# with col2:
#     st.write("Squared")
#     st.dataframe(squared_arr)
    
    
# With st.experimental_memo -----------------------------------------------------
# @st.experimental_memo
# def square(arr):
#     return arr * arr

# squared_arr = square(arr)

# # This works with memo!
# squared_arr[0] = -1

# col1, col2 = st.columns(2)
# with col1:
#     st.write("Original")
#     st.dataframe(arr)
# with col2:
#     st.write("Squared")
#     st.dataframe(squared_arr)


# With st.auto_cache -----------------------------------------------------
@st.auto_cache
def square(arr):
    return arr * arr

squared_arr = square(arr)

# This also works with auto_cache. Simple, it's a numpy array so it serializes it. 
squared_arr[0] = -1

col1, col2 = st.columns(2)
with col1:
    st.write("Original")
    st.dataframe(arr)
with col2:
    st.write("Squared")
    st.dataframe(squared_arr)

