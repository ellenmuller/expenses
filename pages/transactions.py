from utils.sheets import create_connection
from utils.transactions import display_transactions
import streamlit as st

conn = create_connection()
# Cache for 10 minutes
df = conn.read(ttl=600)

st.title("Recent transactions")

with st.popover("Display options"):

    col1, col2 = st.columns(2)

    paid_by = col1.multiselect(label="Paid by", options=["Ellen", "Alex"], default=["Ellen", "Alex"])
    paid_for = col2.multiselect(label="Paid for", options=["Both", "Ellen", "Alex"], default=["Both", "Ellen", "Alex"])
    # date_range = st.date_input(
    #     "Transactions from", 
    #     value=(datetime.date(datetime.datetime.now().year, 1, 1), datetime.datetime.now()),
    #     max_value=datetime.datetime.now(),
    #     format="MM.DD.YYYY"
    # )

df = display_transactions(df, paid_by, paid_for) 
st.dataframe(df)
