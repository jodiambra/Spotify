# import packages
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

st.set_page_config(page_title="Music Awards",
                   page_icon=None,
                   layout='wide',
                   initial_sidebar_state="auto",
                   menu_items=None)
#-----------------------------#
st.title('Music Awards of the Decade')
grammys = pd.read_csv(r'grammys.csv')

grammys.drop('Unnamed: 0', axis=1, inplace=True)
##################################

st.header('Grammy Winners of the Decade')

col1, col2 = st.columns(2)

with col1:
    st.table(grammys)

with col2:
    st.title('')
    image_1 = Image.open('grammy.png')
    st.image(image_1, width=700)



##########################

st.header('American Music Award Winner')

amas = pd.read_csv(r'amas.csv')

amas.drop('Unnamed: 0', axis=1, inplace=True)

col1 , col2 = st.columns(2)

with col1:
    image_2 = Image.open('amas.png')
    st.image(image_2, width=700)

with col2:
    
    st.title('')
    st.title('')
    st.table(amas)


####################################

st.header('Super Bowl Performers')

super_bowl = pd.read_csv(r'super_bowl.csv')
super_bowl.drop('Unnamed: 0', axis=1, inplace=True)
col1 , col2 = st.columns(2)

with col1:

    image_2 = Image.open('super_bowl.png')
    st.image(image_2, width=700)

with col2:
    st.title('')
    st.title('')
    st.title('')
    st.table(super_bowl)

st.title('')
st.title('')

####################################


st.header('Artist Total Cumulative Weeks at Number One')

table3 = pd.read_csv(r'table3.csv')
table3.drop('Unnamed: 0', axis=1, inplace=True)

# total cumulative weeks at number one

st.write(px.histogram(table3, x='artist', y='weeks_at_number_one', height=800, width=900,
    template='plotly_dark', labels={'artist': 'Artists', 'weeks_at_number_one': 'Weeks at Number One'}))


##########################################

st.header('Song Total Number of Weeks at Number One')

table4 = pd.read_csv(r'table4.csv')
table4.drop('Unnamed: 0', axis=1, inplace=True)

col1, col2 = st.columns(2)

# histogram songs total weeks at number 1
with col1:
    st.title('')
    st.write(px.histogram(table4, x='song', y='weeks_at_number_one', height=800, width=700,
    template='ggplot2', labels={'song': 'Song', 'weeks_at_number_one': 'Weeks at Number One'}))

with col2:
    st.table(table4)

###########################################    

st.header('Songs and Artists of Billboard Hot 100')

image_1 = Image.open('billboard_hot_100.png')
st.image(image_1, width=700)
billboard = pd.read_csv(r'billboard.csv')
billboard.drop('Unnamed: 0', axis=1, inplace=True)
st.table(billboard)

st.title('')
st.title('')

#######################################