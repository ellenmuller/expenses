from utils.sheets import create_connection, display_transactions
import streamlit as st

conn = create_connection()
df = conn.read()

st.title("Recent transactions")

col1, col2 = st.columns(2)

paid_by = col1.selectbox("Paid by", ["Either", "Ellen", "Alex"])
paid_for = col2.selectbox("Paid for", ["Both", "Ellen", "Alex"])

display_transactions(df, paid_by, paid_for)