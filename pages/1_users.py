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

st.set_page_config(page_title='Spotify Super Users',
                   page_icon=None,
                   layout='wide',
                   initial_sidebar_state="auto",
                   menu_items=None)
#-----------------------------#


st.title('Spotify Super Users')
# Title Picture

# image_1 = Image.open('streaming-illustration-v-2019-billboard-1548.webp')

# st.image(image_1, width=1000)

# full dataset 
st.header('Spotify Full Dataset')

full = pd.read_csv(r'full_sample.csv')


#########################################################################

#  Most Common Artists of the Decade


st.subheader('Top 5 Most Common Artists of the Decade')

image = Image.open('full images/top 5 most common artists of the decade.png')

st.image(image)

st.title('')

st.subheader('Top 10 Most Common Artists of the Decade')

image1 = Image.open('full images/top 10 most common artists of the decade.png')

st.image(image1)

st.title('')

st.subheader('Top 20 Most Common Artists of the Decade')

image2 = Image.open('full images/top 20 most common artists of the decade.png')

st.image(image2)

st.title('')

st.subheader('Top 50 Most Common Artists of the Decade')

image3 = Image.open('full images/top 50 most common artists of the decade.png')

st.image(image3)

st.title('')

st.subheader('Top 100 Most Common Artists of the Decade')

image4 = Image.open('full images/top 100 most common artists of the decade.png')

st.image(image4)

st.title('')


st.title('')

############################################################################


st.subheader('Top Spotify Listeners')

image5 = Image.open('full images/top spotify listeners.png')

st.image(image5)


st.title('')


st.title('')

st.subheader('Most Listened to Playlists')

image6 = Image.open('full images/5 most common playlists of the decade.png')

st.image(image6)

st.title('')
st.title('')

st.text('We were able to demonstrate trends in the dataset for the most popular artists,')
st.text('most popular playlists, and the most active users. While the dataset does not have')
st.text('any further insights to extract, key insights that we do have are found in the top') 
st.text('artists. Overall, we see that Daft Punk and Coldplay predominate the artist category') 
st.text('on Spotify. Furthermore, it would take days of straight listening to become the number') 
st.text('one user on Spotify. ')

