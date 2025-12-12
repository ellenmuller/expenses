import streamlit as st

def calculate_debt(df):
    paid_by = df.groupby('Paid by')['Value'].sum()
    paid_for = df.groupby('Paid for')['Value'].sum()
    
    people = ['Alex', 'Ellen']
    balance = {}
    
    for person in people:
        paid = paid_by.get(person, 0)
        spent = paid_for.get(person, 0)
        balance[person] = paid - spent

    if 'Both' in paid_for.index:
        both_amount = paid_for['Both'] / 2
        balance['Alex'] -= both_amount
        balance['Ellen'] -= both_amount
    
    return {
        'total': df['Value'].sum(),
        'balance': balance,
        'owes': f"Ellen owes Alex £{balance['Alex']:.2f}" if balance['Alex'] > 0 
                else f"Alex owes Ellen £{-balance['Alex']:.2f}" if balance['Alex'] < 0 
                else "All settled!"
        }