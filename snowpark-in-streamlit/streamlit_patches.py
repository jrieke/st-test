from streamlit import *
import snowflake.snowpark
from millify import millify


MAX_ROWS = 10000


def _handle_snowpark_dataframe(data):
    if isinstance(data, snowflake.snowpark.dataframe.DataFrame):
        num_rows = data.count()
        data = data.take(MAX_ROWS)
        if num_rows > MAX_ROWS:
            caption(f"⚠️ Snowpark dataframe has {millify(num_rows)} rows, showing only first {millify(MAX_ROWS)}.")
    return data



original_dataframe = dataframe
def dataframe(data=None, width=None, height=None):
    data = _handle_snowpark_dataframe(data)
    original_dataframe(data=data, width=width, height=height)
    
    
original_table = table
def table(data=None):
    data = _handle_snowpark_dataframe(data)
    original_table(data=data)
    
    
original_line_chart = line_chart
def line_chart(data=None, width=0, height=0, use_container_width=True):
    data = _handle_snowpark_dataframe(data)
    original_line_chart(data=data)
    
    
original_area_chart = area_chart
def area_chart(data=None, width=0, height=0, use_container_width=True):
    data = _handle_snowpark_dataframe(data)
    original_area_chart(data=data)
    
    
original_bar_chart = bar_chart
def bar_chart(data=None, width=0, height=0, use_container_width=True):
    data = _handle_snowpark_dataframe(data)
    original_bar_chart(data=data)
    

original_write = write
def write(*args, **kwargs):
    if len(args) == 1 and (isinstance(args[0], snowflake.snowpark.dataframe.DataFrame) or (isinstance(args[0], list) and isinstance(args[0][0], snowflake.snowpark.row.Row))):
        dataframe(args[0])
    else:
        original_write(*args, **kwargs)
        