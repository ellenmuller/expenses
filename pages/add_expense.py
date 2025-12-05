from datetime import date
import streamlit as st
from utils.sheets import create_write_connection
import pandas as pd

st.title("Add a new expense")

title = st.text_input("Expense title")
amount = st.text_input("Amount")
paid_by = st.selectbox("Paid by", ["Ellen", "Alex"])

conn = create_write_connection()
df = conn.read()

if title and amount and paid_by:
    if st.button("Add Expense"):
        new_row = pd.DataFrame([{
            "Date": date.today().strftime("%d/%m/%Y"),
            "Description": title,
            "Value": float(amount),
            "Paid by": paid_by,
            "Paid for": None
        }])
        
        # Add to existing DataFrame
        df = pd.concat([df, new_row], ignore_index=True)
        # Save back to sheet
        conn.update(data=df)
        st.write("Expense added!")