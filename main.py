import streamlit as st
import langchain_help as lh


st.title("Youtube Channel Name Generator")
niche = st.sidebar.selectbox("Pick a niche",("Cooking","Gaming","Fashion","Tech reviews","Fitness and wellness"))



if niche:
    response = lh.generate_channel_name_and_topics(niche)
    st.header(response['channel_name'].strip())
    menu_items = response['topics'].strip().split(",")
    st.write("**Trending topics**")
    for item in menu_items:
        st.write("-",item)
