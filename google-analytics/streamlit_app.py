import os

import streamlit as st

"""
# My new app

This is a demo for Google Analytics.
"""


@st.experimental_singleton
def update_index_html():
    def replace_in_file(filename, oldvalue, newvalue):
        # Read in the file
        with open(filename, "r") as f:
            filedata = f.read()

        # Replace the target string
        filedata = filedata.replace(oldvalue, newvalue)

        # Write the file out again
        with open(filename, "w") as f:
            f.write(filedata)

    # Find path to streamlit's index.html.
    st_dir = os.path.dirname(st.__file__)
    index_filename = os.path.join(st_dir, "static", "index.html")

    # Insert tracking code for Google Analytics.
    tag = "G-69G53B780R"
    tracking_code = f"""<!-- Global site tag (gtag.js) - Google Analytics --><script async src="https://www.googletagmanager.com/gtag/js?id={tag}"></script><script>window.dataLayer = window.dataLayer || []; function gtag(){{dataLayer.push(arguments);}} gtag('js', new Date()); gtag('config', '{tag}');</script>"""

    size_before = os.stat(index_filename).st_size
    replace_in_file(index_filename, "<head>", "<head>" + tracking_code)
    size_after = os.stat(index_filename).st_size

    st.write("Inserted tracking code into:", index_filename)
    st.write("Size before:", size_before)
    st.write("Size after: ", size_after)
    
update_index_html()
