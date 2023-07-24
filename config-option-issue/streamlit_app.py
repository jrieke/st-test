import streamlit as st

"""
If you see the error details below, then client.showErrorDetails = true is not working.
If you see the redacted error message, then it is working. test
"""

raise ValueError("This description shouldn't show up if client.showErrorDetails = true is set")
