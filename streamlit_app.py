import streamlit as st
from google.cloud import vision
from PIL import Image
import easyocr

#title
st.title("Easy OCR - Extract Text from Images")

class OCRApp:
    def __init__(self):
        self.google_vision_client = vision.ImageAnnotatorClient()
    
    def run(self):
            st.title("OCR Comparison App")
            image = st.file_uploader("Upload an image", type=["jpg", "png","jpeg"])
    
            if image:
                image_bytes = image.read()
                st.image(image, caption='Uploaded Image.', use_column_width=True)
                st.write("")
                if st.button("Process with Google Cloud Vision"):
                    self.process_google_vision(image_bytes)

    def process_google_vision(self, image_bytes):
            img = vision.Image(content=image_bytes)
            with st.spinner("Running Google Cloud Vision..."):
                response = self.google_vision_client.text_detection(image=img)
            texts = response.text_annotations
            for text in texts:
                description = text.description
                st.write(f"Text: {description}")

if __name__ == "__main__":
    app = OCRApp()
    app.run()
