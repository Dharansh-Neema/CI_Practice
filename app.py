import streamlit as st

st.title("Calculate the Sqaure of a number")
st.write("Enter a number to calculate its square, cube, and fifth power.")


n = st.number_input("Enter a number",value=1,step=1)
# Calculate the Sqaure 
square = n ** 2
cube = n ** 3
fifth = n ** 5
st.write(f"The Sqaure of {n} is: {square}")
st.write(f"The cube of {n} is : {cube}")
st.write(f"The fifth power of {n} is :{fifth}")
