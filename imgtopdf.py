#CNVERTING IMAGE TO PDF USING img2pdf PYTHON LIBRARY

import img2pdf

#IMPORTING IMAGE MODULE FROM PYTHON_IMAGE_LIBRARY(PIL)

from PIL import Image

#IMPORTING easygui FOR FILEOPENBOX FOR SELECTING THE FILE

import easygui

#STORING THE SELECTED FILE PATH IN VARIABLE

fopen=easygui.fileopenbox();

# STORING IMAGE PATH  
img_path = fopen

print("Image Selected Location is : "+fopen)

#TAKING PATH AND FILENAME FROM THE USER

path=input("Enter the path to save your PDF File : ")

filename=input("Enter the Filename to save : ")

# STORING PDF PATH

pdf_path=path+filename+".pdf";

# IMAGE OPENING

image = Image.open(img_path) 

#CONVERTING THE IMAGE INTO CHUNKS USING IMG2PDF LIBRARY

pdf_bytes = img2pdf.convert(image.filename) 

#CREATING THE PDF FILE IF NOT EXISTS OR OPENING THE PDF FILE IF EXISTS

file = open(pdf_path, "wb") 

# WRITING THE PDF FILE WITH CHUNKS

file.write(pdf_bytes) 

# CLOSING THE IMAGE
image.close() 

# CLOSING THE FILE 
file.close() 

# output 
print("Successfully made pdf file in "+pdf_path) 
