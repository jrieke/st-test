import json

import pandas as pd
import streamlit as st
import streamlit_hacks


# With st.cache -----------------------------------------------------
# @st.cache
# def load_csv():
#     return pd.read_csv("pokemon.csv")


# @st.cache
# def load_txt():
#     with open("test.txt") as f:
#         return f.read()


# @st.cache
# def load_json():
#     # read json from test.json and return as dict
#     with open("test.json") as f:
#         return json.load(f)

# csv = load_csv()
# # Shows mutationw warning and exception (since the column doesn't exist anymore).
# # csv.drop("Name", axis=1, inplace=True)
# "### The CSV file"
# csv

# txt = load_txt()
# # Cannot mutate string, so nothing to worry about.
# "### The txt file"
# txt

# js = load_json()
# # Shows mutation warning.
# js["glossary"]["title"] = "changed the title!"
# "### The json file"
# js


# With st.experimental_memo -----------------------------------------------------
# @st.experimental_memo
# def load_csv():
#     return pd.read_csv("pokemon.csv")


# @st.experimental_memo
# def load_txt():
#     with open("test.txt") as f:
#         return f.read()


# @st.experimental_memo
# def load_json():
#     # read json from test.json and return as dict
#     with open("test.json") as f:
#         return json.load(f)

# csv = load_csv()
# # Works.
# csv.drop("Name", axis=1, inplace=True)
# "### The CSV file"
# csv

# txt = load_txt()
# # Cannot mutate string, so nothing to worry about.
# "### The txt file"
# txt

# js = load_json()
# # Works.
# js["glossary"]["title"] = "changed the title!"
# "### The json file"
# js


# With st.auto_cache -----------------------------------------------------
@st.auto_cache
def load_csv():
    return pd.read_csv("pokemon.csv")


@st.auto_cache
def load_txt():
    with open("test.txt") as f:
        return f.read()


@st.auto_cache
def load_json():
    # read json from test.json and return as dict
    with open("test.json") as f:
        return json.load(f)

csv = load_csv()
# Works.
csv.drop("Name", axis=1, inplace=True)
"### The CSV file"
csv

txt = load_txt()
# Cannot mutate string, so nothing to worry about.
"### The txt file"
txt

js = load_json()
# Works.
js["glossary"]["title"] = "changed the title!"
"### The json file"
js