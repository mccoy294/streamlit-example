import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
from PIL import ImageDraw
import easyocr as ocr

# Import the outline_identifier function from the ocr_identification module


st.title('Uber pickups in NYC')

st.text('Upload a file')
uploaded_files = st.file_uploader("Choose an image to upload")
if uploaded_files is not None:
    st.text('image is displaying')

image = Image.open(uploaded_files)
st.image(image, caption='Image to perform OCR Text Extraction')

def outline_identifier(image):
  #store the image input
  img = image
  
  #Call pytesseract as an instance and pass in the image. Store the output as a dictionary of items
  d = pytesseract.image_to_data(img, output_type=Output.DICT)

  #Determine the number of boxes that will have to be drawn
  n_boxes = len(d['text'])
  #Draw the boxes for each text item in the dictionary
  for i in range(n_boxes):
    if float(d['conf'][i]) > 60:  # Check if confidence score is greater than 60
        (x, y, w, h) = (d['left'][i], d['top'][i], d['width'][i], d['height'][i])
        draw = PIL.ImageDraw.Draw(img)
        draw.rectangle((x, y, x + w, y + h), outline=(0, 255, 0), width=2)

  #Show the image
  img.show()

  return img


# Use the outline_identifier function to identify the text in the image
ocr_image = outline_identifier(image)
st.image(ocr_image, caption='Bound each section of the image with these boxes')

DATE_COLUMN = 'date/time'
DATA_URL = ('https://s3-us-west-2.amazonaws.com/'
            'streamlit-demo-data/uber-raw-data-sep14.csv.gz')

@st.cache_data
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    return data

data_load_state = st.text('Loading data...')
data = load_data(10000)
data_load_state.text("Done! (using st.cache_data)")

if st.checkbox('Show raw data', value='show_raw_data'):
    st.subheader('Raw data')
    st.write(data)

st.subheader('Number of pickups by hour')
hist_values = np.histogram(data[DATE_COLUMN].dt.hour, bins=24, range=(0,24))[0]
st.bar_chart(hist_values)

# Some number in the range 0-23
hour_to_filter = st.slider('hour', 0, 23, 17)
filtered_data = data[data[DATE_COLUMN].dt.hour == hour_to_filter]

st.subheader('Map of all pickups at %s:00' % hour_to_filter)
st.map(filtered_data)

with st.echo(code_location='below'):
    total_points = st.slider("Number of points in spiral", 1, 5000, 2000)
    num_turns = st.slider("Number of turns in spiral", 1, 100, 9)

    Point = namedtuple('Point', 'x y')
    data = []

    points_per_turn = total_points / num_turns

    for curr_point_num in range(total_points):
        curr_turn, i = divmod(curr_point_num, points_per_turn)
        angle = (curr_turn + 1) * 2 * math.pi * i / points_per_turn
        radius = curr_point_num / total_points
        x = radius * math.cos(angle)
        y = radius * math.sin(angle)
        data.append(Point(x, y))

    st.altair_chart(alt.Chart(pd.DataFrame(data), height=500, width=500)
        .mark_circle(color='#0068c9', opacity=0.5)
        .encode(x='x:Q', y='y:Q'))
