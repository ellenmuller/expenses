import pandas as pd
    
def display_transactions(df, paid_by=["Ellen", "Alex"], paid_for=["Both", "Alex", "Ellen"]):
    filtered_df = df.copy()
    
    filtered_df = filtered_df[filtered_df['Paid for'].isin(paid_for)]
    
    filtered_df = filtered_df[filtered_df['Paid by'].isin(paid_by)]
    
    # Normalise date column in case of any issues with copy pasting into the sheet
    filtered_df['Date'] = pd.to_datetime(filtered_df['Date'], format='%d-%m-%Y', errors='coerce').dt.date
    
    return filtered_df
