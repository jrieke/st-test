# Note that this needs Python 3.8 for Snowpark!!

import streamlit as st
from snowflake.snowpark import Session
from snowflake.snowpark.functions import col
from contextlib import contextmanager
import time
from millify import millify
import pandas as pd


@contextmanager
def st_timeit(desc=""):
    start = time.time()
    yield
    end = time.time()
    if desc:
        s = desc + " took"
    else:
        s = "Took"
    st.caption(f"{s} {end-start:.2f} s")



@st.experimental_singleton
def create_session():
    return Session.builder.configs(st.secrets.snowflake).create()


session = create_session()
st.write(session)
st.success("Connected to Snowflake! ❄️")


# @st.experimental_memo
# def load_data():
#     table = session.table("SNOWFLAKE_SAMPLE_DATA.TPCDS_SF100TCL.CATALOG_PAGE")
#     table = table.limit(100)
#     return table

def capped_dataframe(data=None, width=None, height=None, max_rows=10000):
    
    # TODO: But how does max_rows work for non-Snowpark dataframes? Could at least limit 
    # the amount of rows we are sending to the frontend?
    # Or should we just make this a config option for now? Could allow to set it via 
    # set_option, so it's also available when developing in Snowsight (since it doesn't 
    # support multiple files for now).
    
    try:
        if max_rows is not None:
            # TODO: count() is only needed for the error message. Should we leave it out?
            # Or at least compute after the dataframe is sent to the frontend?
            with st_timeit("count()"):
                num_rows = data.count()
            if num_rows > max_rows:
                st.caption(f"⚠️ Snowpark dataframe has {millify(num_rows)} rows, showing only first {millify(max_rows)}.")
            
        
        start = time.time()
        data = data.take(max_rows)
        end = time.time()
        st.caption(f"take() took {end-start:.2f} s")
    except AttributeError:
        pass  # not a Snowpark dataframe
    
    with st_timeit("st.dataframe"):
        st.dataframe(data=data)


if st.checkbox("Download data"):
    with st_timeit():
        df = session.table("SNOWFLAKE_SAMPLE_DATA.TPCH_SF1.LINEITEM")#.limit(100)
        # df = df.select(col("CP_CATALOG_PAGE_NUMBER"))  # only one number column

        capped_dataframe(df)
        # df.limit(10000)
        # st.write(df.count())
        # df = df.collect()
        # st.write("Downloaded data, now sending to frontend...")
        # # st.write(type(df[0]))
        # st.dataframe(df)
        # # df = df.to_pandas()
        # # st.selectbox("label", df)
        
# df = session.table("SNOWFLAKE_SAMPLE_DATA.TPCDS_SF100TCL.CATALOG_PAGE").limit(100)
# # df = df.select(col("CP_CATALOG_PAGE_NUMBER"))  # only one number column
# # df = df.collect()
# st.selectbox("label", df)
# st.write(df.to_pandas())
# # st.write(df.columns())
# # pd.DataFrame(df, columns=df.columns())


# import mock
# st.dataframe(mock.df())
# st.selectbox("label", mock.df(3))

