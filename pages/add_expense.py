from datetime import date
import streamlit as st
from utils.sheets import create_connection
import pandas as pd

st.title("Add a new expense")

title = st.text_input("Expense title", placeholder="e.g. 'Cinema tickets'")
amount = st.text_input("Amount", placeholder="£")
paid_by = st.selectbox("Paid by", ["Ellen", "Alex"])
paid_for = st.selectbox("Paid for", ["Both", "Ellen", "Alex"])

conn = create_connection()
df = conn.read()

if title and amount and paid_by and paid_for:
    if st.button("Add Expense"):
        new_row = pd.DataFrame([{
            "Date": date.today().strftime("%d/%m/%Y"),
            "Description": title,
            "Value": float(amount),
            "Paid by": paid_by,
            "Paid for": paid_for
        }])
        
        # TODO Add data type checking for the tables
        # Add to existing DataFrame
        df = pd.concat([df, new_row], ignore_index=True)
        # Save back to sheet
        conn.update(data=df)
        st.write("Expense added!")