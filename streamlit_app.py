import streamlit as st

st.title('My Mom\'s New Healthy Diner')

st.header('Breakfast Menu')

words= ['Omega 3 & Blueberry Oatmeal', 'Kale, Spinach & Rocket Smoothie', 'Hard-Boiled Free_range Egg']
for word in words:
  st.write(word)
