import streamlit as st
import pandas as pd


st.title("Information on text columns")

file_url = ('CSV link')

df = pd.read_csv(file_url, nrows=1000, parse_dates=['Date/Time'])




st.subheader("xxxxx")

"""Display name of column as subtitle
Display number of unique values
Display number of missing values
Display number of rows with empty string
Display number of rows with only whitespaces
Display number of rows with only lower case characters
Display number of rows with only upper case characters
Display number of rows with only alphabet characters
Display number of rows with only numbers as characters
Display the mode value"""


