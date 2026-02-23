import streamlit as st

st.title("Basic Calculator")

n1 = st.number_input("Enter first number :", step=1)
n2 = st.number_input("Enter second number :", step=1)

operation = st.selectbox("Choose operation :",["Addition","Subtraction","Multiplication","Division"])

if st.button("Calculate"):
    if operation == "Addition":
        st.write("Result :",n1+n2)
    elif operation == "Subtraction":
        st.write("Result :",n1-n2)
    elif operation == "Multiplication":
        st.write("Result :",n1*n2)
    else:
        if n2 != 0:
            st.write("Result :",n1/n2)
        else:
            st.write("Error : Division by zero is not allowed.")