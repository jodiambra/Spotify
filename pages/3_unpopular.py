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

st.set_page_config(page_title='Spotify Unpopular Songs',
                   page_icon=None,
                   layout='wide',
                   initial_sidebar_state="auto",
                   menu_items=None)
#-----------------------------#


st.title('Most Unpopular Songs of the Decade')
# Title Picture

# image_1 = Image.open('streaming-illustration-v-2019-billboard-1548.webp')

# st.image(image_1, width=1000)

# unpopular  dataset 
st.header('Spotify Unpopular Dataset Correlation Matrix')
st.cache()
unpopular = pd.read_csv(r'unpopular.csv')

unpopular.drop('Unnamed: 0', axis=1, inplace=True)
st.cache()
st.write(px.imshow(unpopular.corr(), template='simple_white', text_auto=True, 
        aspect='auto', height=1300, width=1400))

with st.expander('Details'):
    st.write('Acousticness has the strongest negative correlation to popularity,', 
            'while danceability, loudness, and explicit have the strongest positive', 
            'correlations. The other metrics have weak correlation values, so they',
            'do not appear to be that important.')

st.title('')

st.title('')

##################################################

st.subheader('Popularity Ratings of Unpopular Songs')

# Popularity Ratings
st.cache()
st.write(px.histogram(unpopular.popularity, title='Popularity Ratings of Unpopular Songs', 
        template='plotly_dark', color_discrete_sequence=['green'], height=900, width=1400))

with st.expander('Details'):
    st.write('We see the values of popularity in this dataset range from 0 to 18, with an', 
            'average of 3.0, and a median of 2.0. This greatly differs from the metrics', 
            'in the top10 dataset, where average popularity was in the 60s. This dataset', 
            'is indeed unpopular, as the distribution is skewed to the right, with most', 
            'values under 3. The mode of the dataset, the most common value, is zero.')

st.title('')

st.title('')

#####################################################

col1, col2 = st.columns(2)

with col1:
    st.title('')

    st.title('')
    image = Image.open('parental advisory.png')
    st.image(image, use_column_width=True)

with col2:
    st.subheader('Are Explicit Songs Less Popular?')

    st.write(px.bar(unpopular.explicit.value_counts(), color=['Explicit', 'Non Explicit'], 
            title='Distribution of Explicit Songs Amongst Unpopular Tracks', 
            template='plotly_dark', color_discrete_sequence=['green', 'white']))

with st.expander('Details'):
    st.write("This illustrates the distribution of explicit lyrics in the songs of", 
            "the unpopular dataset. We see that more songs are not explicit, than", 
            "explicit. However, conclusions can not be made on the basis of a song's", 
            "lack of popularity, solely by its explicit status.")
    st.title('')

    st.title('')



###########################################################
st.subheader('Most Unpopular Songs')

start_numbers, end_numbers = st.select_slider('Select a popularity score', options=range(0,18), value=[0,5])

st.cache()
st.table(unpopular[unpopular['popularity'].between(start_numbers, end_numbers)].sort_values(by='popularity', ascending=True))

with st.expander('Details'):
    st.write('')

