import streamlit as st
import pandas as pd
from src.numeric import NumericColumn
from src.numeric import read_numeric as rn
from src.data import read_data, Dataset

def main():
  st.title('Data Explorer Tool')

  csv_file = st.file_uploader("Choose a CSV file", type=['csv'])
  if csv_file is not None:
    df = pd.read_csv(csv_file)
    # st.success('File uploaded')
    def run_section1():
      read_data(csv_file.name, df)
      show_nrows = st.slider('Select the number of rows to be displayed', 5, 50, 5)
      container1 = st.container()
      select_column = st.multiselect('Which columns do you want to convert to dates', df.select_dtypes(include='object').columns)
      data = Dataset(csv_file.name, df)
      with container1:
        if any(ele in select_column for ele in df.columns):
          for i in select_column:
              df[i] = pd.to_datetime(df[i])
              df.append(df[i])
          st.write('**Top Rows of Table**', data.get_head(show_nrows))
          st.write('**Bottom Rows of Table**', data.get_tail(show_nrows))
          st.write('**Random Sample Rows of Table**', data.get_sample(show_nrows))
        else:
          st.write('**Top Rows of Table**', data.get_head(show_nrows))
          st.write('**Bottom Rows of Table**', data.get_tail(show_nrows))
          st.write('**Random Sample Rows of Table**', data.get_sample(show_nrows))
    
    run_section1()
    st.subheader('2. Information on numeric columns')
    rn(df)
  else:
    # st.warning('No csv file uploaded')
    st.stop()
  



main()