import pandas as pd
import numpy as np
import streamlit as st
import easyocr
import PIL
from PIL import Image, ImageDraw
from matplotlib import pyplot as plt


# main title
st.title("Get text from image with EasyOCR") 
# subtitle
st.markdown("## EasyOCRR with Streamlit")

# upload image file
file = st.file_uploader(label = "Upload your image", type=['png', 'jpg', 'jpeg'])
