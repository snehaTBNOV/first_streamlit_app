import streamlit
import pandas
import snowflake.connector
import requests
from urllib.error import URLError

streamlit.title('Breakfast favourites')

streamlit.header('Breakfast Menu')   
streamlit.text(' 🥣 Omega 3  & Blueberry Oatmeal')
streamlit.text('🥗 Kale Spinach & Rocket smoothie')
streamlit.text('🐔 Hard Boiled egg')
streamlit.text('🥑🍞Avocado toast')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

# Let's put a pick list here so they can pick the fruit they want to include 
#streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))
fruits_selected=streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show=my_fruit_list.loc[fruits_selected]

# Display the table on the page.
#streamlit.dataframe(my_fruit_list)
streamlit.dataframe(fruits_to_show)

#to show fruityvice input
streamlit.header("Fruityvice Fruit Advice!")
#fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
#streamlit.write('The user entered ', fruit_choice)


#to handle error

#try:
 #fruit_choice = streamlit.text_input('What fruit would you like information about?')
 #if not fruit_choice:
   #streamlit.error("please select a fruit to get info")
 #else:
   #fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+fruit_choice)
   #fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
   #streamlit.write(fruityvice_normalized)
#except URLError as e:
 #streamlit.error()

#cretae a repeatable fun of code
def get_fruityvice_data(fruit_choice):
 fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+ fruit_choice)
 fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
 return fruityvice_normalized

try:
 fruit_choice = streamlit.text_input('What fruit would you like information about?')
 if not fruit_choice:
   streamlit.error("please select a fruit to get info")
 else:
  back_from_function=get_fruityvice_data(fruit_choice)
  streamlit.dataframe(back_from_function)

except URLError as e:
 streamlit.error()

#import requests
#fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
#fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+"kiwi")
#fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+fruit_choice)
#streamlit.text(fruityvice_response.json())
# to view the json more nicer
#fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
#streamlit.write(fruityvice_normalized)


'''my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
#my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
my_cur.execute("SELECT * from fruit_load_list")'''
 



streamlit.header("fruit load list contains:")
#snowflake realted function
def get_fruit_load_list():
  with my_cnx.cursor() as my_cur:
   my_cur.execute("SELECT * from fruit_load_list")
   return my_cur.fetchall()

#add a button to load the fruit
if streamlit.button('Get Fruit Load List'):
 my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
 my_data_rows = get_fruit_load_list()
 streamlit.dataframe(my_data_rows)

#my_data_row = my_cur.fetchone()
#my_data_rows = my_cur.fetchall()
#streamlit.text("hello from sf:")
#streamlit.header("fruit load list contains:")
#streamlit.dataframe(my_data_rows)

#add another input
streamlit.header("Fruityvice Fruit Advice!")
add_my_fruit = streamlit.text_input('What fruit would you like to add?','Jackfruit')
streamlit.write('Thanks for adding', add_my_fruit)
streamlit.stop()
my_cur.execute("insert into FRUIT_LOAD_LIST values ('from streamlit')")

