import streamlit as st
import time  # to simulate a real time data, time loop
import numpy as np  # np mean, np random
import pandas as pd  # read csv, df manipulation
#import plotly.express as px  # interactive charts

st.set_page_config(
    page_title="Library Management System",
    page_icon="✅",
    layout="wide",
)

st.title("Library Management System")

warehouse = pd.read_csv('Fact_Table.csv')
windsor = pd.read_csv('Windsor/Borrows_Win.csv')
toronto = pd.read_csv('Toronto/Borrows_To.csv')
ottawa = pd.read_csv('Ottawa/Borrows_Ot.csv')

# top-level filters
database_filter = st.selectbox("Select Database",['Warehouse','Windsor','Toronto', 'Ottawa'])

# dataframe filter
if database_filter == "Warehouse":
    df = warehouse
elif database_filter == "Windsor":
    df = windsor
elif database_filter == "Toronto":
    df = toronto
elif database_filter == "Ottawa":
    df = ottawa

st.dataframe(df)
# user id , isbn , rrent amount, quantity , date
st.write("Insert a New Record")
form = st.form(key='my-form')
User_ID = form.text_input('Enter User_ID')
ISBN = form.text_input('Enter book ISBN')
rent = int(form.number_input('Enter Rent Amount'))
quantity = int(form.number_input('Enter Quantity'))
date = form.date_input("Enter Date of Transaction")

#new_row = {"User_ID":"amurkitt15", "ISBN": "925102302-6", "RentAmount":2, "Quantity":2, "Date":"31/03/2009"}
#toronto_borrows = toronto_borrows.append(new_row, ignore_index=True)

submit = form.form_submit_button('Insert')
if submit:
    st.write(f'Inserting into City: {database_filter} Record User_ID: {User_ID}')
    if database_filter == "Windsor":
        new_row = {"User_ID":User_ID, "ISBN": ISBN, "RentAmount":rent, "Quantity":quantity, "Date":date}
        windsor = windsor.append(new_row, ignore_index=True)
        
    elif database_filter == "Toronto":
        new_row = {"User_ID":User_ID, "ISBN": ISBN, "RentAmount":rent, "Quantity":quantity, "Date":date}
        toronto = toronto.append(new_row, ignore_index=True)
        
        
    elif database_filter == "Ottawa":
        new_row = {"User_ID":User_ID, "ISBN": ISBN, "RentAmount":rent, "Quantity":quantity, "Date":date}
        ottawa = ottawa.append(new_row, ignore_index=True)
