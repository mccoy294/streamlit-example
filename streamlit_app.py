import streamlit as st
from google.cloud import vision
from PIL import Image
import easyocr

#title
st.title("Easy OCR - Extract Text from Images")

class OCRApp:
    def __init__(self):
        st.set_page_config(page_title="OCR App")
        self.google_vision_client = vision.ImageAnnotatorClient()
    
    def run(self):
            st.title("OCR Comparison App")
            image = st.file_uploader("Upload an image", type=["jpg", "png","jpeg"])
    
            if image:
                st.image(image, caption='Uploaded Image.', use_column_width=True)
                st.write("")
                if st.button("Process with Google Cloud Vision"):
                    self.process_google_vision(image)

    def process_google_vision(self, image):
            img = vision.Image(image)
            st.write("Running Google Cloud Vision...")
            content = image.read()
            google_image = vision.Image(content=content)
            response = self.google_vision_client.text_detection(image=google_image)
            texts = response.text_annotations
            for text in texts:
                description = text.description
                st.write(f"Text: {description}")

if __name__ == "__main__":
    app = OCRApp()
    app.run()
