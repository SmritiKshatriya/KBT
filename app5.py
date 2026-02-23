import streamlit as st

st.markdown("""
<style>    
    .stButton > button
    {
    background-color : blue;
    color : white;
    border-radius : 10px;
    }
</style>
 
    
""",unsafe_allow_html=True)



st.title("Basics of Streamlit")

age = st.slider("Enter your age",1,100)

city  = st.selectbox("Select your city",["Nashik","Pune","Mumbai","Delhi","Chandigarh","Banglore"])

if st.button("Show details"):
    st.write("Your age is :",age)
    st.write("Your city is :",city)