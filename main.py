import streamlit as st
from cache.session_state import init_session_state

init_session_state()

st.title('Verificador de Café')
st.title("")



if st.session_state.image != None:
    st.subheader("Preview image:")
    st.image(st.session_state.image,use_column_width=True)
    
    c1,c2 = st.columns(2)

    with c1: 
        if st.button("Predict Image",use_container_width=True):
            pass

    with c2: 
        if st.button("Delete Image",use_container_width=True):
            st.session_state.image = None
            st.experimental_rerun()

else:
    st.session_state.image = st.file_uploader("Image",type=['png', 'jpg'])
    st.button("Continue",use_container_width=True)

