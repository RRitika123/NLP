import streamlit as st
import langchain_help as lh


st.title("Restaurant Name Generator")
cuisine = st.sidebar.selectbox("Pick a Cuisine",("Indian","Italian","Maxican","Arabic","American"))



if cuisine:
    response = lh.generate_restaurant_name_and_items(cuisine)
    st.header(response['restaurant_name'].strip())
    menu_items = response['menu_items'].strip().split(",")
    st.write("**Menu Items**")
    for item in menu_items:
        st.write("-",item)