from dataclasses import dataclass
from pandas import Series,DataFrame
import streamlit as st
import pandas as pd
from scr.numeric import NumericColumn
from scr.numeric import rd_numeric as rn
from src.data import read_data, Dataset

st.title('Data Explorer Tool')

csv_file = st.file_uploader("Choose a CSV file")
if csv_file is not None:
    df = pd.read_csv(csv_file)
else:
    st.stop()

def run_section1():
  read_data(csv_file.name, df)
  show_nrows = st.slider('Select the number of rows to be displayed', 5, 50, 5)
  container1 = st.container()
  select_column = st.multiselect('Which columns do you want to convert to dates', df.select_dtypes(include='object').columns)
  with container1:
    if any(ele in select_column for ele in df.columns):
      for i in select_column:
          df[i] = pd.to_datetime(df[i])
          df.append(df[i])
      st.write('**Top Rows of Table**', Dataset.get_head(df, show_nrows))
      st.write('**Bottom Rows of Table**', Dataset.get_tail(df, show_nrows))
      st.write('**Random Sample Rows of Table**', Dataset.get_sample(df, show_nrows))
    else:
      st.write('**Top Rows of Table**', Dataset.get_head(df, show_nrows))
      st.write('**Bottom Rows of Table**', Dataset.get_tail(df, show_nrows))
      st.write('**Random Sample Rows of Table**', Dataset.get_sample(df, show_nrows))

run_section1()

st.title('2. Numeric Column Information')
rn(df)