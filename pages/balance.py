import streamlit as st
from utils.sheets import create_connection, calculate_debt

st.title("The Hoare Treasury")

conn = create_connection()

df = conn.read()

current_balance = calculate_debt(df)

fair_share = current_balance['total']/2

ellen_balance = current_balance['Ellen']-fair_share
if ellen_balance <0:
    message = f"Currently Ellen owes {ellen_balance}"
else:
    alex_balance = current_balance['Alex']-fair_share
    message = f"Currently Alex owes {alex_balance }"

col1, col2 = st.columns([3, 1])

col1.subheader(message)
col2.image('budgeting.png')

