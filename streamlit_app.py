import streamlit as st
from google.cloud import vision
from PIL import Image
import easyocr

#title
st.title("Easy OCR - Extract Text from Images")

google_vision_client = vision.ImageAnnotatorClient()

st.title("OCR Comparison APP")
iamge = st.file_uploader("Upload an image",type = ['jpg','jpeg','png'])

img = Image.open(image)

st.write("Running Google Cloud Vision...")
content = image.read()
google_image = vision.Image(content=content)
response = self.google_vision_client.text_detection(image=google_image)
texts = response.text_annotations
for text in texts:
        description = text.description
        st.write(f"Text: {description}")
