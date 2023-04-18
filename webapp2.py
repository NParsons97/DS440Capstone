# -*- coding: utf-8 -*-
"""Webapp2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1osh4zpMRvsOThUWoegWvqgfsUT9pwaSq
"""

import streamlit as st
import numpy as np
from PIL import Image 
import tensorflow as tf
from tensorflow.keras.models import load_model


 
from tempfile import NamedTemporaryFile
from tensorflow.keras.preprocessing import image 

st.set_option('deprecation.showfileUploaderEncoding', False)
@st.cache(allow_output_mutation=True)

def loading_model():
  fp = "cnn_pneu_vamp_models.h5"
  model_loader = load_model(fp)
  return model_loader

cnn = loading_model()
st.write("""
# X-Ray Classification (Pneumonia/Normal)
""")


types = ['jpg', 'jpeg', 'webp', 'png']
  


temp = st.file_uploader("Upload X-Ray Image", type = types)

buffer = temp
temp_file = NamedTemporaryFile(delete=False)
if buffer:
    temp_file.write(buffer.getvalue())
    st.write(image.load_img(temp_file.name))


if buffer is None:
  st.text("Please Upload an Image")

else:

 

  img = image.load_img(temp_file.name, target_size=(500, 500),color_mode='grayscale')

  # Preprocessing the image
  pp_img = image.img_to_array(img)
  pp_img = pp_img/255
  pp_img = np.expand_dims(pp_img, axis=0)

  #predict
  preds= cnn.predict(pp_img)
  if preds >= 0.2:
    out = ('{:.2%} confident that this is Pneumonia'.format(preds[0][0]))
  
  else: 
    out = ('{:.2%} confident that this is Normal'.format(1-preds[0][0]))

  st.success(out)
  
  image = Image.open(temp)
  st.image(image,use_column_width=True)