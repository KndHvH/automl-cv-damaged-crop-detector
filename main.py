import streamlit as st
import cv2
import numpy as np
from cache.session_state import init_session_state
from model.predict import predict_image


init_session_state()

st.title('Verificador de Café')
st.title("")



if st.session_state.image is not None:
    st.subheader("Preview image:")
    st.image(st.session_state.image,use_column_width=True)
    
    c1,c2 = st.columns(2)

    with c1: 
        if st.button("Predict Image",use_container_width=True):
            image = cv2.resize(st.session_state.image, (224, 224)) 
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            predict = predict_image(image)
            st.text(predict)

    with c2: 
        if st.button("Delete Image",use_container_width=True):
            st.session_state.image = None
            st.experimental_rerun()

else:
    uploaded_file = st.file_uploader("Image", type=['png', 'jpg'])
    if uploaded_file is not None:
        file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
        image = cv2.imdecode(file_bytes, 1)
        st.session_state.image = image
    st.button("Continue",use_container_width=True)

