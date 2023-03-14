import streamlit as st
from PIL import Image

st.title("BasketBall Information Portal")
st.subheader("By Bradley")
option = st.selectbox("Select the player you want to view", ["Lebron James", "Ja Morant", "Kobe Bryant", "Kyrie Irving"])
if option == "Lebron James":
    st.subheader("Lebron James")
    st.image("lebron.jfif")
    col1, col2, col3 = st.columns(3)
    col1.metric("Age", "38 years", "Current")
    col2.metric("Height", "6'9", "2.06 m")
    col3.metric("Weight", "113kg", "249.1 pounds" )

if option == "Ja Morant":
    st.subheader("Ja Morant")
    st.image("ja.jfif")
    col1, col2, col3 = st.columns(3)
    col1.metric("Age", "23 years", "Current")
    col2.metric("Height", "6'2", "1.88m")
    col3.metric("Weight", "79kg", "174.1 pounds" )

if option == "Kobe Bryant":
    st.subheader("Kobe Bryant")
    st.image("kOBE.jfif")
    col1, col2, col3 = st.columns(3)
    col1.metric("Age", "42 years", "Died(2020)")
    col2.metric("Height", "6'6", "1.98m")
    col3.metric("Weight", "96kg", "211.6 pounds" )

if option == "Kyrie Irving":
    st.subheader("Kyrie Irving ")
    st.image("Anklebreaker.jfif")
    col1, col2, col3 = st.columns(3)
    col1.metric("Age", "30 years", "Current")
    col2.metric("Height", "6'2", "1.88m")
    col3.metric("Weight", "88kg", "194 pounds" )
