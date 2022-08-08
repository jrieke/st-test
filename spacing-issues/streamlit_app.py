import streamlit as st
import numpy as np


hacks = st.checkbox("Add hacks")
if hacks:
    st.write(
        """
        <style>
        [data-testid="stHorizontalBlock"] {
            gap: 1rem;
            flex-wrap: nowrap; 
        }
        
        label:empty {
            display: none;
        }
        
        [data-testid="stMetricLabel"] {
            display: none;
        }
        
        [data-baseweb="slider"] {
            padding-left: 6px;
            padding-right: 6px;
        }
        /*
        [role="checkbox"] {
            width: 1.2rem;
            height: 1.2rem;
        }
        
        
        [data-baseweb="checkbox"] {
            padding-top: 9px;
            padding-bottom: 9px;
        }
        */
        
        /*
        
        [data-baseweb="select"] > div > div {
            padding-top: 6px;
            padding-bottom: 6px;
        }
        
        [data-baseweb="input"] > div > input {
            padding-top: 6px;
            padding-bottom: 6px;
        }
        
        button,[kind="primary"] {
            padding-top: 7px !important;
            padding-bottom: 7px !important;
        }
        
        .stNumberInput > div > div:nth-child(2) {
            height: 42px;
        }
        */
        
        
        </style>
        """, 
    unsafe_allow_html=True)
else:
    st.write("")
    
"---"
st.info("Header + st.metric without label. There's a weird space between the header and metric.")

st.header("Predicted revenue")
st.metric("", "$ 13.20 mio", "+ 8 % yoy")

"---"

st.info("Bunch of text inputs without label. The space between the inputs shouldn't be there.")

st.write("Enter your favorite Streamlit commands below:")
st.text_input("")
st.text_input("", key="2")
st.text_input("", key="3")
st.text_input("", key="4")
st.text_input("", key="5")

"---"

st.info("Image + header side by side. The gap between image and header is too low.")

col1, col2 = st.columns(2)
col1.image("https://asset.bloomnation.com/c_pad,d_vendor:global:catalog:product:image.png,f_auto,fl_preserve_transparency,q_auto/v1649823367/vendor/364/catalog/product/s/h/shutterstock_90055534_30.jpg")
col2.header("Balloons")
col2.write("Here are some balloons. They are round and colorful.")

"---"

st.info("Widget with label and without label in st.columns. Impossible to get it to align properly, even with empyty st.write('').")

col1, col2 = st.columns(2)
col1.selectbox("Select something", ["option 1", "option 2"])
col2.button("Click here!")

"---"

st.info("Pager widget from metrics app. Should vertically align in the middle but it's impossible to get that.")
col1, col2, col3, _ = st.columns([1, 2, 1, 4])
col1.button("<")
col2.write("29 May to 04 June")
col3.button(">")

"---"

st.info("Space between code and chart seems very small. This is the same issue as in st.tabs.")
st.code("st.line_chart(...)")
np.random.seed(1)
st.line_chart(np.random.rand(10, 2))

"---"

st.info("Same for st.dataframe. Especially since the space to a widget is larger, see below.")
st.code("st.dataframe(...)")
np.random.seed(1)
st.dataframe(np.random.rand(10, 2))

st.code("st.dataframe(...)")
st.slider("Random widget")

"---"

st.info("Padding between the form and st.metric here seems a bit too small. But then again, if we make the padding below forms/expanders very large, it's annoying if you have e.g. multiple expanders.")

with st.form("foo"):
    st.text_area("Write something here")
    st.form_submit_button()
col1, col2, col3 = st.columns(3)
col1.metric("Number", 310, "+ 10 % yoy")
col2.metric("Number", 310, "+ 10 % yoy")
col3.metric("Number", 310, "+ 10 % yoy")

"---"

st.info("Just some expanders to check the padding between them. See above.")
st.expander("Expand me").write("sdf")
st.expander("Expand some more").write("sldkf")
st.expander("Expand some more more").write("sldkf")

"---"


col1, col2, col3 = st.columns(3)
col1.selectbox("Select", ["Option 1", "Option 2", "Option 3"])
col1.text_input("Write")
col1.checkbox("Check here")
col2.selectbox("Select 2", ["Option 1", "Option 2", "Option 3"])
col2.slider("Slide it")
col3.selectbox("Select 3", ["Option 1", "Option 2", "Option 3"])
# col2.checkbox("Checkbox", True)
# col3.text_input("", key="6")


def space(px):
    st.write(f'<div style="height: {px}px;"></div>', unsafe_allow_html=True)



st.write("---")
col1, col2, col3, col4 = st.columns(4)
col1.selectbox("Select sth", ["Option 1", "Option 2", "Option 3"])
# col2.text_input(" ", key="sdf")
if hacks:
    with col2:
        space(27)
col2.checkbox("Check me")
if hacks:
    with col3:
        space(31)
col3.button("Click me")


# col1, col2, col3, col4 = st.columns(4)
# col1.text_input("", key="ssdfdf")
# col2.text_input("", key="sdsdff")
# with col3:
#     space(1)
# col3.checkbox("foo")
# col4.button("Click me again")


st.write("")
st.checkbox("Check this here")
st.checkbox("And this")
st.checkbox("Or you can check this")

st.number_input("Number")


col1, col2 = st.sidebar.columns(2)
col1.selectbox("Selects lksdklf", ["Option 1", "Option 2", "Option 3"])
col2.text_input("skldf")


col1, col2 = st.columns(2)
col1.selectbox("Select something", ["option 1", "option 2"])
col2.button("Click here!")