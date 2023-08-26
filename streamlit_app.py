import streamlit as st
import cv2
import PIL
import numpy as np
import easyocr

st.title('🎈 App Name 1')

st.write('Hello world!')

def cleanup_text(text):
	# strip out non-ASCII text so we can draw the text on the image
	# using OpenCV
	return "".join([c if ord(c) < 128 else "" for c in text]).strip()


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
	
    # OCR the input image using EasyOCR
    st.write("[INFO] OCR'ing input image...")
    reader = easyocr.Reader("en")
    results = reader.readtext(image)


    # loop over the results
    for (bbox, text, prob) in results:
	# display the OCR'd text and associated probability
	#print("[INFO] {:.4f}: {}".format(prob, text))
	# unpack the bounding box
	(tl, tr, br, bl) = bbox
	tl = (int(tl[0]), int(tl[1]))
	tr = (int(tr[0]), int(tr[1]))
	br = (int(br[0]), int(br[1]))
	bl = (int(bl[0]), int(bl[1]))
	# cleanup the text and draw the box surrounding the text along
	# with the OCR'd text itself
	text = cleanup_text(text)
	cv2.rectangle(image, tl, br, (0, 255, 0), 2)
	cv2.putText(image, text, (tl[0], tl[1] - 10),
		cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)

	st.image(image)




