import streamlit as st
from google.cloud import vision
from PIL import Image
import easyocr

#title
st.title("Easy OCR - Extract Text from Images")

google_vision_client = vision.ImageAnnotatorClient()

st.title("OCR Comparison APP")
image = st.file_uploader("Upload an image", type=["jpg","jpeg","png"])

if image is not None:
    img = vision.Image(image)
