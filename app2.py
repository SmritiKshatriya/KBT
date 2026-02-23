import streamlit as st

st.title("Basics of Streamlit")

age = st.slider("Enter your age",1,100)

city  = st.selectbox("Select your city",["Nashik","Pune","Mumbai","Delhi","Chandigarh","Banglore"])

if st.button("Show details"):
    st.write("Your age is :",age)
    st.write("Your city is :",city)