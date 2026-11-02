import streamlit as st
from logic import greet

st.title("Hello App")
name = st.text_input("What is your name?")
if name: 
	st.write(greet(name))


from logic import add

st.subheader("Add two numbers")
a  = st.number_input("First number", value=0.0)
b = st.number_input(Second number", value=0.0)
if st.button("Add"):
	st.write(f"{a} + {b} = {add(a, b)}")