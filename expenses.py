import streamlit as st

pages = {
    "": [
        st.Page("pages/balance.py", title="Balance", icon="💰", default=True), 
        st.Page("pages/transactions.py", title="Transactions", icon="📊"),
        st.Page("pages/add_expense.py", title="Add Expense", icon="💵")
    ],
}

pg = st.navigation(pages)
pg.run()