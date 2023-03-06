import streamlit as st

# with st.form("my_form"):
#     name = st.text_input("Name")
#     age = st.number_input("Age", 0, 120, 18)
#     st.form_submit_button("Submit")


def verify_age():
    if st.session_state.age < 18:
        show_dialog("You are not old enough!")
        st.stop()


def show_dialog(error_msg=None):
    print("Showing dialog")
    dialog = st.dialog("my_dialog", can_be_closed=False)
    with dialog:
        if error_msg:
            st.error(error_msg)
        name = st.text_input("Name")
        age = st.number_input("Age", 0, 120, 18, key="age")
        st.form_submit_button("Submit", on_click=verify_age)
    dialog.open()
    return name, age


if st.button("Enter personal information"):
    #name, age = show_dialog()
    #st.write(f"Your name is {name} and you are {age} years old.")
    
    dialog = st.dialog("my_dialog", can_be_closed=False)
    with dialog:
        name = st.text_input("Name")
        age = st.number_input("Age", 0, 120, 18, key="age")
        st.form_submit_button("Submit")

    dialog.open()

st.write(f"Your name is {name} and you are {age} years old.")

# if age < 18:
#     st.error("You are not old enough!")
#     dialog.open()
# else:
#     st.write(f"Your name is {name} and you are {age} years old.")


# Option 1: Dialog is just like a form. No open/close method. 
if st.button("Open dialog"):
    with st.dialog("my_dialog"):
        name = st.text_input("Name")
        age = st.number_input("Age", 0, 120, 18, key="age")
        st.form_submit_button("Submit")
    
    
# Option 2: Dialog has open/close method.
dial = st.dialog("my_dialog_2")
with dial:
    name = st.text_input("Name")
    age = st.number_input("Age", 0, 120, 18, key="age")
    st.form_submit_button("Submit")

if st.button("Open dialog 2"):
    dial.open()

# Option 3: Just open, no close. 
dial = st.dialog("my_dialog_3")
with dial:
    name = st.text_input("Name")
    age = st.number_input("Age", 0, 120, 18, key="age")
    st.form_submit_button("Submit")
    
if st.button("Open dialog 3"):
    dial.open()
    
# Cool thing about this: you can do validation a) without using callbacks/session state 
# and b) without the closing behavior changing based on whether there is a callback or not.
# Instead, dialog always closes if X or submit button is clicked.
dial = st.dialog("my_dialog_3_validation")
with dial:
    name = st.text_input("Name")
    age = st.number_input("Age", 0, 120, 18)
    submitted = st.form_submit_button("Submit")
    
if st.button("Open dialog 3"):
    dial.open()
    
if submitted and age < 18:
    dial.error("You are not old enough!")  # shows an error in the dialog below submit
    dial.open()