import time

import numpy as np
import pandas as pd
import streamlit as st

css = st.container()

with st.sidebar:
    # show_spinner = st.checkbox("Show spinner", True)
    function_time = st.number_input("Runtime of cached function", value=2.0)
    if st.checkbox("Make spinner overlap, using gradient"):
        css.markdown(
            """
            <style>
                div:has(> .stSpinner), div:has(> .stProgress) {
                    height: 0;
                    overflow: visible;
                    visibility: visible;
                    margin-bottom: -1rem;
                    z-index: 1000;
                }
                
                .stSpinner, .stProgress {
                    /* current design in the official figma */
                    background: linear-gradient(180deg, #FFF 72%, rgba(255, 255, 255, 0.00) 100%);
                    padding: 1rem 0;
                    margin-top: -1rem;
                    
                }
            </style>
            """,
            unsafe_allow_html=True,
        )
    if st.checkbox("Make spinner overlap, using shadow"):
        css.markdown(
            """
            <style>
                div:has(> .stSpinner), div:has(> .stProgress) {
                    height: 0;
                    overflow: visible;
                    visibility: visible;
                    margin-bottom: -1rem;
                    z-index: 1000;
                }
                
                .stSpinner, .stProgress {
                    /* Show it similar to toolbar with shadow. Looks weird. */
                    
                    padding: 0.25rem 0.5rem;
                    background-color: white;
                    box-shadow: 1px 2px 8px rgba(0, 0, 0, 0.08); 
                    width: 280px !important;
                    border-radius: 0.5rem;
                    
                }
            </style>
            """,
            unsafe_allow_html=True,
        )
    if st.checkbox("Make spinner smaller"):
        css.markdown(
            """
            <style>
            .stSpinner i {
                width: 1.25rem;
                height: 1.25rem;
            }
            .stSpinner > div {
                gap: 0.5rem;
            }
            </style>
            """,
            unsafe_allow_html=True,
        )

    show_delay = st.checkbox("Show spinner after delay")
    delay_time = st.number_input("Delay", value=0.5, disabled=not show_delay)
    if not show_delay:
        delay_time = 0
    st.sidebar.button("🏃‍♀️ Rerun app")
    
def spin_it(mock_func_name):
    # if show_spinner:
    if function_time < delay_time:
        time.sleep(function_time)
    else:
        time.sleep(delay_time)
        with st.spinner(f"Running `{mock_func_name}`."):
            time.sleep(function_time - delay_time)
    # else:
    #     time.sleep(function_time)
        
# content = st.container()
# if st.sidebar.button("🗑️ Clear content"):
#     content.empty()
# with content:
"Here is some text:"
spin_it("loading_text_data")
"Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."

"Here is a dataframe:"
spin_it("loading_dataframe_data")
df = pd.DataFrame(np.random.randn(50, 20), columns=("col %d" % i for i in range(20)))
st.dataframe(df)  # Same as st.write(df)

"Here is a chart:"
spin_it("loading_chart_data")
st.bar_chart(df)



# col1, col2 = st.columns(2)
# actual_runtime = col1.number_input("Function runtime", value=3)
# estimated_runtime = col2.number_input("Estimated runtime", value=2)

# p = st.progress(0, text="Running `load_data_1()`.")
# for i in np.arange(0, actual_runtime, 0.1):
#     if i < 0.8*estimated_runtime:
#         p.progress(i / estimated_runtime, text="Running `load_data_1()`.")
#     else:
#         p.progress(0.8, text="Running `load_data_1()`.")
#     time.sleep(0.1)


# for i in np.arange(0, 0.8*estimated_runtime, 0.1):
#     p.progress(i / estimated_runtime, text="Running `load_data_1()`.")
#     time.sleep(0.1)
#     if actual_runtime < i:
#         break

# remaining_time = actual_runtime - 0.8*estimated_runtime
# if remaining_time > 0:
#     for i in np.arange(0, remaining_time, 0.1):

#         time.sleep(0.1)


#     # np.logspace(np.log10(0.8*estimated_runtime), np.log10(estimated_runtime), 100):
#     #     #print(i)
#     #     p.progress(i / estimated_runtime, text="Running `load_data_1()`.")
#     #     time.sleep(0.01)
#     #     if actual_runtime < i:
#     #         break


# p.empty()
