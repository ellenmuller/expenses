from utils.sheets import create_connection, display_transactions

conn = create_connection()

df = conn.read()

display_transactions(df)