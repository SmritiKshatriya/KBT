import streamlit as st

st.markdown("""
    <style>
        .stButton > button
            {
            background-color : green;
            color : white;
            border-radius : 10px;
            border : 2px solid white;
            }
      
    </style>
    
""",unsafe_allow_html=True)

st.title("Basic Form")

name = st.text_input("Enter your name")
mail = st.text_input("Enter your email")
pswd = st.text_input("Enter your password",type="password")
gender = st.radio("Select your gender",["Male","Female","Prefer not to say"])
contact = st.number_input("Enter your contact number",step = 1)

if st.button("Submit"):
    st.write("Hello ",name)
    st.write("Your email is ",mail)
    st.write("Your password is ",pswd)
    st.write("Your gender is ",gender)
    st.write("Your contact number is ",contact)