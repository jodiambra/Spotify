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

st.set_page_config(page_title='Spotify Exploratory Data Analysis',
                   page_icon=None,
                   layout='wide',
                   initial_sidebar_state="auto",
                   menu_items=None)
#-----------------------------#


st.title('Spotify Exploratory Data Analysis')
# Title Picture

image_1 = Image.open('streaming-illustration-v-2019-billboard-1548.webp')

st.image(image_1, width=1000)

#-------------------------------#
st.title('')

st.title('')


# full  dataset 
st.header('Spotify Full Snippet Dataset')

full = pd.read_csv(r'full_sample.csv')

st.dataframe(full.head(10))

with st.expander('Details'):
    st.write('We see the full dataset is very large, comprised of columns : user id, artist name, track name, and', 
        'playlist name. We have a small percentage of missing values in artist name, and we will get rid of all the', 
        'missing values in the dataset. With artist name having the most missing values, but less than half a percent', 
        'is actually missing, the other datasets will have a miniscule number of missing values as well. We look', 
        'at the number of unique artists, which attests that the vast majority of artists appear more than once. We also', 
        'take a list view of the most popular artists, and the most popular playlists. ')
    

st.title('')

st.title('')



# Top 10 dataset 
st.header('Spotify Top 10 Dataset')

top10 = pd.read_csv(r'top_10.csv')

st.dataframe(top10)

with st.expander('Details'):
    st.subheader('Average Popularity of Each Year')
    years = [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019]
    for i in years:
        means = top10[top10['year']== i]['pop'].mean()
        
        st.write(str(i) + '  :  ' + str(means))

st.title('')

st.title('')

########################################################

# Unpopular dataset 

st.header('Spotify Unpopular Dataset')

unpopular = pd.read_csv(r'unpopular.csv')

st.dataframe(unpopular)

with st.expander('Details'):
    st.write('The unpopular dataset has a similar structure to the top 10 dataset, but with a few different features.', 
            'This dataset does not have any missing vales, and does not appear to have duplicates. We see Swishahouse', 
            'has 3 songs named "Freestyle," yet the metrics associated with each song is different. This supports the', 
            'theory that they are in fact different songs with the same name. ')
st.title('')

st.title('')