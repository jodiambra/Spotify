#import packages
import streamlit as st
import pandas as pd
import plotly_express as px
from PIL import Image
from streamlit.commands.page_config import Layout
from scipy import stats as stat

#----------------------------#
# Upgrade streamlit library
# pip install --upgrade streamlit

#-----------------------------#
# Page layout

st.set_page_config(page_title='Spotify Miscellaneous Analysis',
                   page_icon=None,
                   layout='wide',
                   initial_sidebar_state="auto",
                   menu_items=None)
#-----------------------------#


st.title('Spotify Over the Decade')

# Title Picture

# image_1 = Image.open('streaming-illustration-v-2019-billboard-1548.webp')

# st.image(image_1, width=1000)


# full  dataset 
st.cache()
full = pd.read_csv(r'full_sample.csv')

# Top 10 dataset 
st.cache()
top10 = pd.read_csv(r'top_10.csv')

# unpopular dataset
st.cache()
unpopular = pd.read_csv(r'unpopular.csv')

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

st.subheader('Songs Ranked by Popularity')

numbers = st.select_slider('Select a number of artists', options=range(95, 5, -5))

st.cache()
st.table(top10[top10['pop'] > numbers].sort_values(by='pop', ascending=False))


with st.expander('Details'):
    st.write('Widening the filter to a minimum popularity score of 85,', 
            'we start to see songs from other years. Yet, the top songs are',
            'dominated by the year 2019.')

st.title('')

st.title('')


#########################################

st.subheader('Statistical Difference from 2019 Popularity')

st.cache()
selections = st.selectbox('What year do you want to look at', [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019])

st.subheader('')
# 2019 and 2018

st.cache()
if selections == 2010:
    st.write('p-value:  5.064237674160785e-11.', 
            'We reject the null hypothesis, the popularity', 
            'means of the 2019 and 2010 are different')
if selections == 2011:
    st.write('p-value:  2.1903598698159695e-10.', 
            'We reject the null hypothesis, the popularity', 
            'means of the 2019 and 2011 are different')
if selections == 2012:
    st.write('p-value:  4.904997717800578e-07.', 
            'We reject the null hypothesis, the popularity', 
            'means of the 2019 and 2012 are different')
if selections == 2013:
    st.write('p-value:  1.3900754415255492e-12.', 
            'We reject the null hypothesis, the popularity', 
            'means of the 2019 and 2013 are different')
if selections == 2014:
    st.write('p-value:  1.9202416636017074e-10.', 
            'We reject the null hypothesis, the popularity', 
            'means of the 2019 and 2014 are different')
if selections == 2015:
    st.write('p-value:  3.411716576167158e-11.', 
            'We reject the null hypothesis, the popularity', 
            'means of the 2019 and 2015 are different')
if selections == 2016:
    st.write('p-value:  1.6466011433742306e-09.', 
            'We reject the null hypothesis, the popularity', 
            'means of the 2019 and 2016 are different')
if selections == 2017:
    st.write('p-value:  6.31211007525009e-10.', 
            'We reject the null hypothesis, the popularity', 
            'means of the 2019 and 2017 are different')
if selections == 2018:
    st.write('p-value:  9.08140589747621e-08.', 
            'We reject the null hypothesis, the popularity', 
            'means of the 2019 and 2018 are different')

st.subheader('')

with st.expander('Details'):
    st.write('It appears that the songs from 2019 are generally more popular', 
            'than songs from other years. Furthermore, the average popularity of the songs', 
            'in 2019 are greater than that of the other years. Statistical', 
            'testing proves that the mean of 2019 is different than the', 
            'means of the other years. This illustrates whey we see a', 
            'positive correlation between year and popularity. ')