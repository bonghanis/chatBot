import streamlit as st

st.title(f"Today's counsel")

# Get your input for OpenAI API key
api_eky = st.text_input("Please input your OpenAI Key:", type = "password")