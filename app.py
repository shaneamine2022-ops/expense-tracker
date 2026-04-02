import streamlit as st
import pandas as pd

st.title("Personal Expense Tracker")

# Load data
try:
    df = pd.read_csv("expenses.csv")
except:
    df = pd.DataFrame(columns=["Date", "Amount", "Category"])

# Inputs
date = st.date_input("Select Date")
amount = st.number_input("Enter Amount (£)")
category = st.selectbox("Category", ["Food", "Travel", "Shopping", "Bills", "Entertainment"])

# Add expense
if st.button("Add Expense"):
    new_data = pd.DataFrame([[date, amount, category]],
                            columns=["Date", "Amount", "Category"])
    df = pd.concat([df, new_data], ignore_index=True)
    df.to_csv("expenses.csv", index=False)
    st.success("Expense Added!")

# Show table
st.subheader("Expense Table")
st.write(df)

# Totals
st.subheader("Total Spending by Category")
totals = df.groupby("Category")["Amount"].sum()
st.write(totals)

# Bar chart
st.subheader("Expense Chart")
st.bar_chart(totals)

# Overall total
st.subheader("Overall Total")
st.write(f"£{df['Amount']}")