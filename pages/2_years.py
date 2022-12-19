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

# Top 10 dataset 
st.header('Spotify Top 10 Dataset')

top10 = pd.read_csv(r'top10.csv')

# rename top genre to genre
top10.rename(columns={'top genre': 'genre'}, inplace=True)

# remove unnamed column
top10 = top10.drop('Unnamed: 0', axis=1)


st.dataframe(top10)

with st.expander('Details'):
    st.subheader('Average Popularity of Each Year')
    years = [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019]
    for i in years:
        means = top10[top10['year']== i]['pop'].mean()
        
        st.write(str(i) + '  :  ' + str(means))

st.title('')

st.title('')

##########################################


#########################

st.subheader('Artist Popularity Based on Year')

# Artist Popularity Based on Year
st.write(px.histogram(top10, y='pop', x='artist', color='year', 
        title='Artist Popularity Based on Year', template='plotly_dark', 
        labels={'pop': 'Popularity', 'artist': 'Artist'}, height=900, width=1400))

with st.expander('Details'):
    st.write('Here, we see the popularity ratings of artists across the years 2010 to 2019. We can', 
            'filter the figure by year, to see new artists that appear in the top 10, as well as artists', 
            'that remain from previous years. Since the metric is the sum of popularity, all the songs of an artist,', 
            'in that particular year, are considered. Therefore, an artist with more songs can sometimes beat an artist', 
            'with a higher popularity rating, all dependant on the total popularity score. Better comparisons can be made when', 
            'isolating the individual years from the dataset, or another view, by comparing the mean popularity scores.')

st.title('')

st.title('')
######################################

# artist, year, popularity pivot
artist_pivot = pd.pivot_table(top10, index='artist', columns='year', values='pop', aggfunc='mean')

# popularity by year interactive
st.write(px.scatter(artist_pivot, animation_frame='year', title='Artist Mean Popularity by Year', 
        template='plotly_dark', color_discrete_sequence=['green'], 
        labels={'value': 'Mean Popularity', 'artist': 'Artist'}, height=900, width=1400))

with st.expander('Details'):
    st.write('By comparing mean instead of total popularity scores, we are able to account for artists with more representation',
            'in the dataset for a particular year. Now, we can truly visualize the differences in artist popularity over the years.',
            'Consequently, artists need to have somewhat of consistency in high scores, as a song that makes the list, that is not very',
            'popular, can lower the respective artists ratings. ')


st.title('')


st.title('')

####################################


# Most popular artists of N year

st.subheader('Most popular Artists of the Decade')

options = st.multiselect('What years do you want to look at', [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019])

for option in options:
    yr = top10[top10.year.isin([option])]
    st.write(px.histogram(yr, y='pop', x='artist', title='Most Popular Artists of ' + str(option), 
        template='plotly_dark', color_discrete_sequence=['green'], labels={'pop': 'Popularity', 'artist': 'Artist'}, 
        height=800, width=1400))
    with st.expander('Details'):
        st.write('Now, filtering by year, we are able to clearly see the top artists of the various periods.',
            'Once again, we are dealing with totals, therefore we see the artists with more songs from a particular', 
            'year in the dataset have higher popularity scores. This is intuitive to what we want to see, a sum of', 
            'popularity rather than a comparison of means, as an artist with multiple hits may garner more popularity',
            'than an artist with one hit in the year. Some artists appear to have a breakout year, where they have multiple', 
            'hit songs. It would stand to reason that Many of these artists have won some type of award or topped multiple', 
            'music charts. Our research further supports this claim.')

st.title('')


# The different years
st.subheader('2010')

st.write()

