import streamlit as st
from PIL import Image
import keras_ocr

#title
st.title("Easy OCR - Extract Text from Images")

class OCRApp:
    def __init__(self):
        pass
    
    def run(self):
            st.title("OCR Comparison App")
            image = st.file_uploader("Upload an image", type=["jpg", "png","jpeg"])
    
            if image:
                image_bytes = image.read()
                image = Image.open(io.BytesIO(image_bytes))
                st.image(image, caption='Uploaded Image.', use_column_width=True)
                st.write("")
                if st.button("Process with Keras-OCR and Pillow"):
                    self.process_keras_ocr_pillow(image)

    def process_keras_ocr_pillow(self, image):
            reader = keras_ocr.Reader(['en'])
            detection_boxes, recognition_boxes, text = reader.readtext(image)
            for i in range(len(text)):
                st.write(text[i])

if __name__ == "__main__":
    app = OCRApp()
    app.run()
