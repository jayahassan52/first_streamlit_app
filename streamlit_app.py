import streamlit
import pandas



streamlit.title('My Parents New Healthy Dinner')
streamlit.header ('Breakfast Favorities')
streamlit.text ('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text ('🥗Kale, Spinach & Rocket Smooothie')
streamlit.text ('🐔Hard-Boiled Free-Range Eggs')
streamlit.text ('🥑🍞 Avacado Toast')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')




my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
my_fruit_list = my_fruit_list.set_index('Fruit')
# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))
fruits_to_show = my_fruit_list.loc[fruits_selected]





streamlit.header("Fruityvice Fruit Advice!")

fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
streamlit.write('The user entered ', fruit_choice)

import requests

fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)



# write your own comment -what does the next line do? 
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# write your own comment - what does this do?
streamlit.dataframe(fruityvice_normalized)

fruits = []

# Create an input field.
fruit_input = st.text_input("Enter a fruit to add to the list.")

# Add an event handler for the input field's on_change event.
if fruit_input:
  fruits.append(fruit_input)

# Display the list of fruits.
st.write("Fruits:", fruits)

import snowflake.connector

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("select * from pc_rivery_db.public.fruit_load_list")
my_data_rows = my_cur.fetchall()
streamlit.text("the fruit load list contains:")
streamlit.text(my_data_rows)

my_data_row = my_cur.fetchone()
streamlit.header("the fruit load list contains:")
streamlit.dataframe(my_data_rows)

# Display the table on the page.




