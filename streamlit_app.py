import streamlit as st
import keras_ocr

# Load the OCR model
model = keras_ocr.load_model("model.h5")

# Create a text analysis function
def text_analysis(text):
  # Recognize the text in the image
  recognized_text = model.recognize(text)

  # Print the recognized text
  print(recognized_text)

# Create a Streamlit app
st.title("Text Analysis App")

# Upload an image
image = st.file_uploader("Upload an image")

# If an image is uploaded, analyze the text
if image is not None:
  image = cv2.imdecode(np.fromstring(image.read(), np.uint8), cv2.IMREAD_COLOR)
  text = keras_ocr.preprocess_image(image)
  text_analysis(text)

