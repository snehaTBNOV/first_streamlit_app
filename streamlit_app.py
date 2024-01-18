import streamlit
import pandas

streamlit.title('Breakfast favourites')

streamlit.header('Breakfast Menu')   
streamlit.text(' 🥣 Omega 3  & Blueberry Oatmeal')
streamlit.text('🥗 Kale Spinach & Rocket smoothie')
streamlit.text('🐔 Hard Boiled egg')
streamlit.text('🥑🍞Avocado toast')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
