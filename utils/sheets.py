from streamlit_gsheets import GSheetsConnection
import streamlit as st

def create_connection():
    conn = st.connection("gsheets", type=GSheetsConnection)
    return conn

def calculate_debt(df):
    contributed = {'Alex': 0, 'Ellen': 0, 'total': 0}
    for row in df.itertuples():
        # st.write(row)
        contributed['total']+= (row[3])
        if row[4]=='Ellen':
            contributed['Ellen']+= (row[3])
        elif row[4]=='Alex':
            contributed['Alex']+= (row[3])
        else:
            st.error("something went wrong!")
    
    return contributed
    
def display_transactions(df):
    st.dataframe(df)
