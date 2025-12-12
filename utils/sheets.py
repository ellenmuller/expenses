from streamlit_gsheets import GSheetsConnection
import streamlit as st

def create_connection():
    conn = st.connection("gsheets", type=GSheetsConnection)
    return conn
    
