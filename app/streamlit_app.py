import streamlit as st
import pandas as pd
from src.numeric import NumericColumn
from src.numeric import read_numeric as rn

csv_file = st.file_uploader("Choose a CSV file")
if csv_file is not None:
    df = pd.read_csv(csv_file)
    st.title('2. Numeric Column Information')
    rn(df)

else:
    st.write('No csv file uploaded')