import streamlit as st
import datetime
    
def display_transactions(df, paid_by=["Ellen", "Alex"], paid_for=["Both", "Alex", "Ellen"]):
                        #  date_range=None):
    filtered_df = df.copy()
    
    filtered_df = filtered_df[filtered_df['Paid for'].isin(paid_for)]
    
    filtered_df = filtered_df[filtered_df['Paid by'].isin(paid_by)]
    
    return filtered_df
    
    # # Filter by date range if provided
    # if date_range is not None:
    #     start_date, end_date = date_range
    #     # start_date = datetime.datetime.strptime(start_date, "YYYY-MM-DD").date()
    #     # end_date = datetime.datetime.strptime(end_date, "YYYY-MM-DD").date()
    #     st.write(filtered_df['Date'][0])
    #     # Ensure the date column is datetime type
    #     filtered_df['Date'] = filtered_df['Date'].apply(lambda x: datetime.datetime.strptime(x, "MM-DD-YYYY").date())
    #     # pd.to_datetime(filtered_df['Date'])
    #     filtered_df = filtered_df[(filtered_df['Date'] >= start_date) & (filtered_df['Date'] <= end_date)]
    