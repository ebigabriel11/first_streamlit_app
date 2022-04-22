import streamlit as st

st.title('My Mom\'s New Healthy Diner')

st.header('Breakfast Favorites')

breakfast= ['🥣 Omega 3 & Blueberry Oatmeal', '🥗 Kale, Spinach & Rocket Smoothie', '🐔 Hard-Boiled Free_range Egg','🥑🍞 Avocado Toast']
for meal in breakfast:
  st.text(meal)

st.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
