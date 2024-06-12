import streamlit as st
import os

def modelName():
    return "gpt-3.5-turbo-0125"

def display_source_code(fineName):
    current_file_path = os.path.abspath(__file__)
    pages_file_path = os.path.join(os.path.dirname(current_file_path),'pages', fineName)
    with open(pages_file_path, 'r', encoding = 'utf-8') as file:
        source_code = file.read()

    st.code(source_code, language = 'python')

def view_sourcecode(fileName):
    if 'show_source_code' not in st.session_state:
        st.session_state.show_source_code = False

    if st.button('Toggle Source Code'):
        st.session_state.show_source_code = not st.session_state.show_source_code

    if st.session_state.show_source_code:
        display_source_code(fileName)

def modelName_embedding_small():
    return "text-embedding-3-small"

def modelName4o():
    return "gpt-3.5-turbo-0125"