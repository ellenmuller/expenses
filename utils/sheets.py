from streamlit_gsheets import GSheetsConnection
import streamlit as st


def create_connection():
    # Create a connection object.
    conn = st.connection("gsheets", type=GSheetsConnection)

    df = conn.read()
    
    return df

def create_write_connection():
    # Create a connection object.
    conn = st.connection("gsheets", type=GSheetsConnection)
    return conn

def calculate_debt(df):
    debt = {'Alex': 0, 'Elex': 0}
    for row in df.itertuples():
        if row[4]=="E":
            debt['E']+= (row[3])
        elif row[4]=='A':
            debt['A']+= (row[3])
        else:
            debt['A']+= (row[3]/2)
            debt['E']+= (row[3]/2)
            
    return debt
    
def display_transactions(df):
    st.dataframe(df)
