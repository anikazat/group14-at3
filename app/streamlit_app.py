import streamlit as st
import pandas as pd
from src.numeric import read_numeric
from src.data import read_data
from src.datetime import rd_dtime
from src.text import text_main


def main():

  # App title
  st.title('Data Explorer Tool')

  # Load csv file
  csv_file = st.file_uploader("Choose a CSV file", type=['csv'])
  if csv_file is not None:
    df = pd.read_csv(csv_file)
    
    # Run section 1: Overall Information
    read_data(csv_file.name, df)

    # Run section 2: Numeric Column Information
    st.header('2. Numeric Column Information')
    read_numeric(df)

    # Run section 3: Text Column Information 
    st.header('3. Text Column Information')
    text_main(df)

    # Run section 4: Datetime Column Information
    st.header('4. Datetime Column Information')
    rd_dtime(df)

  else:
    st.stop()
  



if __name__ == "__main__":
  main()
