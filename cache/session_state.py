import streamlit as st

def init_session_state():
    if 'image' not in st.session_state:
        st.session_state.image = None