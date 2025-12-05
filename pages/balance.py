import streamlit as st
from utils.sheets import create_connection, calculate_debt


st.title("Welcome to Alex and Ellens expenses")

df = create_connection()

current_balance = calculate_debt(df)

st.markdown(f"The current balance is {current_balance}")
