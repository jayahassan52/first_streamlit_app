import streamlit



streamlit.title('My Parents New Healthy Dinner')
streamlit.header ('Breakfast Favorities')
streamlit.text ('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text ('🥗Kale, Spinach & Rocket Smooothie')
streamlit.text ('🐔Hard-Boiled Free-Range Eggs')
streamlit.text ('🥑🍞 Avacado Toast')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')




import pandas
streamlit.dataframe(my_fruit_list)
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
