import streamlit as st
import pandas as pd

st.title('My Mom\'s New Healthy Diner')

st.header('Breakfast Favorites')

breakfast= ['🥣 Omega 3 & Blueberry Oatmeal', '🥗 Kale, Spinach & Rocket Smoothie', '🐔 Hard-Boiled Free_range Egg','🥑🍞 Avocado Toast']
for meal in breakfast:
  st.text(meal)

st.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

my_fruit_list = pd.read_csv('https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt')
st.dataframe(my_fruit_list)
