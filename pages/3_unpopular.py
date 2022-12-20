#import packages
import streamlit as st
import pandas as pd
import plotly_express as px
from PIL import Image
from streamlit.commands.page_config import Layout


#----------------------------#
# Upgrade streamlit library
# pip install --upgrade streamlit

#-----------------------------#
# Page layout

st.set_page_config(page_title='Spotify Over the Decade',
                   page_icon=None,
                   layout='wide',
                   initial_sidebar_state="auto",
                   menu_items=None)
#-----------------------------#


st.title('Spotify Over the Decade')
# Title Picture

# image_1 = Image.open('streaming-illustration-v-2019-billboard-1548.webp')

# st.image(image_1, width=1000)

# unpopular  dataset 
st.header('Spotify Unpopular Dataset')

unpopular = pd.read_csv(r'unpopular.csv')
