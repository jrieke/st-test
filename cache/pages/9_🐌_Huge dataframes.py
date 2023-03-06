import time

import numpy as np
import pandas as pd
import streamlit as st
import streamlit_hacks


@st.experimental_singleton
def create_df(num_rows):
    return pd.DataFrame(
        np.random.randint(0, 100, size=(num_rows, 4)), columns=list("ABCD")
    )


num_rows = 500000000
start_time = time.time()
df = create_df(num_rows)
duration = time.time() - start_time
f"Created dataframe with {len(df)} rows in {duration:.2f} s"

# With st.cache -----------------------------------------------------
# @st.cache
# def filter_type(df, type):
#     return df[(df["Type 1"] == type) | (df["Type 1"] == type)]


# type_ = st.selectbox("Only show pokemon of type...", df["Type 1"].unique())
# df = filter_type(df, type_)

# # This throws CachedObjectMutationWarning with st.cache, since we are modifying the
# # cached object.
# # df.drop("Defense", axis=1, inplace=True)

# st.dataframe(df)


# With st.experimental_memo --------------------------------------------------
# @st.experimental_memo
# def filter_type(df, type):
#     return df[(df["Type 1"] == type) | (df["Type 1"] == type)]


# type_ = st.selectbox("Only show pokemon of type...", df["Type 1"].unique())
# df = filter_type(df, type_)

# # With memo, this works!
# df.drop("Defense", axis=1, inplace=True)

# st.dataframe(df)


# With st.auto_cache --------------------------------------------------
# @st.auto_cache
# def filter_type(df, type):
#     return df[(df["Type 1"] == type) | (df["Type 1"] == type)]


# type_ = st.selectbox("Only show pokemon of type...", df["Type 1"].unique())
# df = filter_type(df, type_)

# # With auto_cache, this works too. Easy case, it recognizes a dataframe, so it serializes
# # it.
# df.drop("Defense", axis=1, inplace=True)

# st.dataframe(df)
