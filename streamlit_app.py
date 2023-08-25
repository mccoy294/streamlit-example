import streamlit as st
import cv2
import PIL

#title
st.title("Simple Image Processing with OpenCV")

# Upload an image
image = st.file_uploader("Upload an image", type=["jpg", "png","jpeg"])

# If an image is uploaded, show it and do some basic processing
if image:
    image_string = str(image)
    img = cv2.imread(image_string)
    img = Image.fromarray(img)
    st.image(img)

    # Convert the image to grayscale
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    st.image(gray_img)

    # Apply a blur to the image
    blurred_img = cv2.GaussianBlur(gray_img, (5, 5), 0)
    st.image(blurred_img)

    # Edge detection
    edges = cv2.Canny(blurred_img, 50, 150)
    st.image(edges)


