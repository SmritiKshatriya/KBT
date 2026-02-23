import streamlit as st

st.title("Dummy Chatbot")

q = st.text_input("Ask me anything..!")

if st.button("Ask"):
    st.write("You asked :",q)
    st.write("Chatbot is processing your query...")
    