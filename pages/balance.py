import streamlit as st
from utils.sheets import create_connection
from utils.debt import calculate_debt

st.title("The Hoare Treasury")

conn = create_connection()

df = conn.read()

current_balance = calculate_debt(df)

col1, col2 = st.columns([3, 1])

col1.subheader(current_balance['owes'])
col2.image('budgeting.png')

