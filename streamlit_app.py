import streamlit as st

st.title("Temperature Converter")
temp_input = st.number_input("Enter temperature value:")
conv_type = st.selectbox("Select conversion type:", ("Celsius to Fahrenheit","Fahrenheit to Celsius"))
