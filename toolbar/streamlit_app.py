import streamlit as st

"""
# Dataframe toolbar

This demo shows the dataframe toolbar in different real-world scenarios.
"""

toolbar_position = st.radio(
    "Toolbar position", ["Hide", "Original prototype", "Hover", "Top right", "Left", "Right"]
)

if toolbar_position == "Hide":
    st.write(
        """
        <style>
        [data-testid="StyledFullScreenButton"] {
            visibility: hidden;
        }
    
        .stDataFrame > :first-child {
            display: none;
        }
        """,
        unsafe_allow_html=True,
    )
elif toolbar_position == "Hover":
    st.write(
        """
        <style>
        [data-testid="StyledFullScreenButton"] {
            visibility: hidden;
        }
        
        .stDataFrame {
            margin-top: 1rem;
        }
        
        /* Initial styles */
        .stDataFrame > :first-child {
            height: 0;
            opacity: 0;
            top: -1.25rem;
            right: 0rem;
            position: absolute;
            z-index: 1000; /* To place it above the second child */
            overflow: hidden;
            margin-bottom: 0;
            transition: opacity 0.3s, top 0.15s;
        }

        /* Styles when parent div is hovered */
        .stDataFrame:hover > :first-child,
        .stDataFrame > :first-child:hover {
            height: auto;
            opacity: 1;
            z-index: 1000;
            top: -1.75rem;
        }

        /* Styles for the second child */
        .stDataFrame > :nth-child(2) {
            position: relative; /* To establish a stacking context */
            z-index: 0; /* To place it below the first child */
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

elif toolbar_position == "Top right":
    st.write(
        """
        <style>
        [data-testid="StyledFullScreenButton"] {
            visibility: hidden;
        }
        
        /* Initial styles */
        .stDataFrame > :first-child {
            height: 0;
            opacity: 0;
            top: -1.5rem;
            right: 0rem;
            position: absolute;
            z-index: 1000; /* To place it above the second child */
            overflow: hidden;
            margin-bottom: 0;
            transition: opacity 0.3s, top 0.15s;
            box-shadow: 1px 2px 8px rgba(0, 0, 0, 0.08);  
            border-radius: 0.5rem;
            background-color: white;
        }

        /* Styles when parent div is hovered */
        .stDataFrame:hover > :first-child,
        .stDataFrame > :first-child:hover {
            height: auto;
            opacity: 1;
            z-index: 1000;
            top: -2.1rem;
        }

        /* Styles for the second child */
        .stDataFrame > :nth-child(2) {
            position: relative; /* To establish a stacking context */
            z-index: 0; /* To place it below the first child */
        }
        </style>
        """,
        unsafe_allow_html=True,
    )


elif toolbar_position == "Left":
    st.write(
        """
        <style>
        [data-testid="StyledFullScreenButton"] {
            visibility: hidden;
        }
        
        /* Initial styles */
        .stDataFrame > :first-child {
            height: 0;
            opacity: 0;
            top: 0rem;
            left: -2rem;
            right: auto;
            position: absolute;
            z-index: 1000; /* To place it above the second child */
            overflow: hidden;
            margin-bottom: 0;
            transition: opacity 0.3s;
            background-color: white;
            box-shadow: 1px 2px 8px rgba(0, 0, 0, 0.08);  
            border-radius: 0.5rem;
            flex-direction: column;
        }

        /* Styles when parent div is hovered */
        .stDataFrame:hover > :first-child,
        .stDataFrame > :first-child:hover {
            height: auto;
            opacity: 1;
            z-index: 1000;
        }

        /* Styles for the second child */
        .stDataFrame > :nth-child(2) {
            position: relative; /* To establish a stacking context */
            z-index: 0; /* To place it below the first child */
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

elif toolbar_position == "Right":
    st.write(
        """
        <style>
        /* Hide the old fullscreen button */
        [data-testid="StyledFullScreenButton"] {
            visibility: hidden;
        }
    
        /* Set the initial style of the toolbar while the dataframe is not hovered */
        .stDataFrame > :first-child {
            height: 0;
            opacity: 0;
            position: absolute;
            top: 0rem;
            right: -1.5rem;
            z-index: 3; /* To place it above the second child, the actual dataframe */
            margin-bottom: 0;
            background-color: white;
            box-shadow: 1px 2px 8px rgba(0, 0, 0, 0.08);  
            border-radius: 0.5rem;
            flex-direction: column;
        }

        /* Set the style of the toolbar when the dataframe or the toolbar is hovered */
        .stDataFrame:hover > :first-child,
        .stDataFrame > :first-child:hover {
            height: auto;
            opacity: 1;
            right: -2rem;
            transition: opacity 0.3s, right 0.15s;
        }

        /* Styles for the actual dataframe content */
        .stDataFrame > :nth-child(2) {
            position: relative; /* To establish a stacking context */
            z-index: 1; /* To place it below the first child */
        }
        
        /* Add a before element on the right side of the dataframe, so you can hover 
           over the gap between the dataframe and the toolbar */
        .stDataFrame::before {
            content: "";
            position: absolute;
            top: -1rem;
            right: -3rem; 
            bottom: 0;
            width: 4rem; 
            pointer-events: none;
            z-index: 2; /* below the first child */
        }

        /* Only capture pointer events like hover on the before element after the 
           dataframe was hovered*/
        .stDataFrame:hover::before {
            pointer-events: auto;
        }
        
        .stButton {
            margin-top: -25px;
        }
        
        .stButton button {
            border-color: #EAEAEB;
            border-radius: 0 0 0.5rem 0.5rem;
            border-top: 1px solid transparent;
            padding-top: 0.4rem;
            padding-bottom: 0.4rem;
            background: 
        }
        
        .stButton p {
            font-size: 14px;
        }
        
        [data-testid="stDataFrameResizable"] {
            border-radius: 0.5rem 0.5rem 0 0 !important;
        }

        
        </style>
        """,
        unsafe_allow_html=True,
    )


# Create a dictionary of data
data = {
    "Name": ["Alice", "Bob", "Charlie", "David"],
    "Age": [25, 30, 35, 40],
    "Occupation": ["Engineer", "Doctor", "Artist", "Teacher"],
}
st.dataframe(data)
st.dataframe(data, use_container_width=True)

col1, col2 = st.columns(2)
col1.dataframe(data, use_container_width=True)
col2.dataframe(data, use_container_width=True)

col1, col2, col3, col4 = st.columns(4)
col1.dataframe(data, use_container_width=True)
col2.dataframe(data, use_container_width=True)
col3.dataframe(data, use_container_width=True)
col4.dataframe(data, use_container_width=True)

with st.form(key="form"):
    st.dataframe(data, use_container_width=True)
    st.form_submit_button("Submit")

with st.expander("Expand", expanded=True):
    st.dataframe(data, use_container_width=True)

tab1, tab2, tab3 = st.tabs(["Tab 1", "Tab 2", "Tab 3"])
tab1.dataframe(data, use_container_width=True)
tab2.dataframe(data, use_container_width=True)
tab3.dataframe(data, use_container_width=True)

long_data = {
    "Name": [
        "Alice",
        "Bob",
        "Charlie",
        "David",
        "Alice",
        "Bob",
        "Charlie",
        "David",
        "Alice",
        "Bob",
        "Charlie",
        "David",
    ],
    "Age": [25, 30, 35, 40, 25, 30, 35, 40, 25, 30, 35, 40],
    "Occupation": [
        "Engineer",
        "Doctor",
        "Artist",
        "Teacher",
        "Engineer",
        "Doctor",
        "Artist",
        "Teacher",
        "Engineer",
        "Doctor",
        "Artist",
        "Teacher",
    ],
}
st.data_editor(long_data, num_rows="dynamic", use_container_width=True)
st.button("\- Delete row", use_container_width=True)

st.sidebar.dataframe(data)
col1, col2 = st.sidebar.columns(2)
col1.dataframe(data)
col2.dataframe(data)
