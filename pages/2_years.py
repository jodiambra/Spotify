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

st.cache()
top10 = pd.read_csv(r'top_10.csv')


######################################

# artist, year, popularity pivot
artist_pivot = pd.pivot_table(top10, index='artist', columns='year', values='pop', aggfunc='mean')

# popularity by year interactive
st.cache()
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

st.subheader('Most Popular Artists of the Decade')


options = st.multiselect('What years do you want to look at', [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019])

st.cache()
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

st.title('')

st.title('')

st.title('')

st.title('')

st.title('')

st.title('')

st.title('')

st.title('')

st.title('')

#######################################################

# The different years

st.subheader('Most Popular Songs of the Decade')

selections = st.selectbox('What year do you want to look at', [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019])

# Most popular artists of N year

st.cache()
yr = top10[top10.year.isin([selections])].nlargest(10, columns='pop')
st.write(px.histogram(yr, y='pop', x='title', title='Most Popular Songs of ' + str(selections), height=800, width=1400,
        template='plotly_dark', color_discrete_sequence=['green'], labels={'pop': 'Popularity', 'title': 'Song Titles'}))
with st.expander('Details'):
    st.write('Here, we compare the popularity, within the various time frames, of the various songs. These songs correspond to', 
            'the top artists of each year, and some artists are represented more than others, with multiple songs on each list. The', 
            'popularity values are relatively close to one another, given the same year. It would not be a stretch to assume these', 
            'songs have topped music charts, or have lead to their respective artists winning a music award. Our research further',
            'supports this claim. ')

st.title('')

st.title('')

############################################################

# Top N artists of the Decade

st.subheader('Most Prolific Artists of the Decade in Top 10')

numbers = st.select_slider('Select a number of artists', options=range(5,101))

st.cache()
top_artist = top10.artist.value_counts().nlargest(numbers)
st.write(px.bar(top_artist, title='Top ' + str(numbers) +  ' Artists of the Decade', height=900, width=1300, 
        template='plotly_dark', color_discrete_sequence=['green'], labels={'index': 'Artists', 'value': 'Number of Songs'}))

with st.expander('Details'):
    st.write('These artists are the top artists of the decade, in the sense that they have the most songs that made the top 10 list.',
    'Looking at the top 5, we see Katy perry, Justin Bieber, Rihanna, Maroon 5 and Lady Gaga. When lengthening the number of artists,',
    'we can see the scale at which the top five are more popular than the rest. Looking across the years, we see many of these artists',
    'appear multiple times in a particular year, and multiple times across a year. ')


############################################

st.subheader('Top 10 Dataset Correlation Matrix')
st.write(px.imshow(top10.corr(), text_auto=True, aspect='auto', height=1300, width=1400, template='seaborn'))

with st.expander('Details'):
    st.write('Correlation matrix shows year, dance and decibels have the highest correlation to popularity. However, we must', 
            'not make the logical fallacy to conclude that correlation means causation. This data simply illustrates a', 
            'relationship between these factors and popularity. Then, we have many metrics that show a negative correlation to',
            'popularity. The key metric with such a relationship includes the duration of the song. Other negatively correlated', 
            'metrics show minimal significance. We can also see the correlations between the metrics, with the other metrics, yet', 
            'our key target is popularity.  ')


####################################################