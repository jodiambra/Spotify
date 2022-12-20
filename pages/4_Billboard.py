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
    st.table(super_bowl)


####################################

st.header('Songs and Artists of Billboard Hot 100')

image_1 = Image.open('billboard_hot_100.png')
st.image(image_1, width=700)
billboard = pd.read_csv(r'billboard.csv')
billboard.drop('Unnamed: 0', axis=1, inplace=True)
st.table(billboard)