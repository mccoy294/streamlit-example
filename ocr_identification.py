import cv2
import pytesseract
from pytesseract import Output


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
        img = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

  #Show the image
  cv2.imshow(img)
  
