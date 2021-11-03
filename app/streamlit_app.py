import sys
import os
if os.path.abspath(".") not in sys.path: 
  sys.path.append(os.path.abspath("."))

from dataclasses import dataclass
from pandas import Series,DataFrame
import streamlit as st
import pandas as pd
from scr.numeric import NumericColumn
from scr.numeric import rd_numeric as rn

csv_file = st.file_uploader("Choose a CSV file")
if csv_file is not None:
    df = pd.read_csv(csv_file)
    st.title('2. Numeric Column Information')
    rn(df)
else:
    st.stop()
