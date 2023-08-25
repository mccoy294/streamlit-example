import streamlit as st
import cv2
import PIL

import streamlit as st

st.title('🎈 App Name')

st.write('Hello world!')

uploaded_file = st.file_uploader("Choose a image file", type = ["jpg","jpeg","png"])
if uploaded_file is not None:
    image = uploaded_file.read()
    img = st.image(image)
