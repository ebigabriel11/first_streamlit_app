import streamlit as st
import pandas as pd

st.title('My Mom\'s New Healthy Diner')

st.header('Breakfast Favorites')

#put all breakfast in a list
breakfast= ['🥣 Omega 3 & Blueberry Oatmeal', '🥗 Kale, Spinach & Rocket Smoothie', '🐔 Hard-Boiled Free_range Egg','🥑🍞 Avocado Toast']

#loop through breakfast list 
for meal in breakfast:
  st.text(meal)

st.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

#get the menu from source aand assign to variable
my_fruit_list = pd.read_csv('https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt')
my_fruit_list = my_fruit_list.set_index('Fruit')

#let's put a pick list here so they can pick the food they want to include
st.multiselect('Pick some fruits', list(my_fruit_list.index))

#show the table ont the page
st.dataframe(my_fruit_list)


