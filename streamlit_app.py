import streamlit as st
import cv2
import PIL
import numpy as np

import streamlit as st

st.title('🎈 App Name')

st.write('Hello world!')

uploaded_file = st.file_uploader("Choose an image file", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Read the uploaded image using PIL
    image = PIL.Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image', use_column_width=True)

    # Convert PIL image to OpenCV format (numpy array)
    img_cv = np.array(image)

    # Convert the image from BGR to RGB (OpenCV uses BGR)
    img_rgb = cv2.cvtColor(img_cv, cv2.COLOR_BGR2RGB)

    # Convert the image to grayscale
    gray = cv2.cvtColor(img_rgb, cv2.COLOR_RGB2GRAY)

    # Display the grayscale image using Streamlit
    st.image(gray, caption='Grayscale Image', use_column_width=True)




