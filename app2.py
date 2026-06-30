import streamlit as st
import numpy as np

st.title("add two numbers")
num1 = st.number_input("Enter the first number", value=0.0)
num2 = st.number_input("Enter the second number", value=0.0)

if st.button("Add"):
    result = num1 + num2
    st.success(f"The sum is: {result}")