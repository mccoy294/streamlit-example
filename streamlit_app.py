import streamlit as st
import cv2
import PIL

#title
st.title("Simple Image Processing with OpenCV 3")

# Upload an image
image = st.file_uploader("Upload an image", type=["jpg", "png","jpeg"])
st.image(image)

