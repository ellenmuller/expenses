from utils.sheets import create_connection, display_transactions

df = create_connection()

display_transactions(df)