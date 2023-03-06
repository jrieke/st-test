import streamlit as st
from transformers import pipeline
import numpy as np

# With st.cache -------------------------------
# Throws UnhashableTypeError. And one which is pretty confusing.
# "Cannot hash object of type tokenizers.Tokenizer, found in the return value of load_model()."
# @st.cache
# def load_model():
#     model = pipeline("fill-mask", model="bert-base-uncased")
#     return model


# model = load_model()
# result = model("Hello I'm a [MASK] model.")
# st.write(result)


# With st.singleton -------------------------------
# Works!
# Note: for this specific model, it actually works with memo as well!! 
# But not the case e.g. with a tensorflow session.
# @st.experimental_memo
# def load_model():
#     model = pipeline("fill-mask", model="bert-base-uncased")
#     return model


# model = load_model()
# result = model("Hello I'm a [MASK] model.")
# st.write(result)


# With st.auto_cache -------------------------------
# Works!
# @st.auto_cache
# def load_model():
#     model = pipeline("fill-mask", model="bert-base-uncased")
#     return model


# model = load_model()
# result = model("Hello I'm a [MASK] model.")
# st.write(result)


# With st.global_state -------------------------------
# Works!
if "model" not in st.global_state:
    st.global_state.model = pipeline("fill-mask", model="bert-base-uncased")


result = st.global_state.model("Hello I'm a [MASK] model.")
st.write(result)

