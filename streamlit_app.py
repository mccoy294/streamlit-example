import streamlit as st
import cv2
import PIL
import numpy as np

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

    # Blur the image using GaussianBlur
    blurred = cv2.GaussianBlur(gray, (7, 7), 0)
    
    #Use addaptive Threholding to make a better image
    thresh = cv2.adaptiveThreshold(blurred, 255,
	cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 21, 4)

    # Display the grayscale image using Streamlit
    st.image(thresh, caption='Threshold Image', use_column_width=True)




