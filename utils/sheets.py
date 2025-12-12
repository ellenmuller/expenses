from streamlit_gsheets import GSheetsConnection
import streamlit as st

def create_connection():
    conn = st.connection("gsheets", type=GSheetsConnection)
    return conn
    
def display_transactions(df, paid_by="Either", paid_for="Both"):
    filtered_df = df[df['Paid for'] == paid_for]
    if paid_by == "Either":
        st.dataframe(filtered_df)
    else:
        filtered_df = filtered_df[filtered_df['Paid by'] == paid_by]
        st.dataframe(filtered_df)
    
