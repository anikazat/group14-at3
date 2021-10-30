# To be filled by students
from numpy import datetime64
import streamlit as st
from dataclasses import dataclass
import pandas as pd


@dataclass
class DateColumn:
  col_name: str
  serie: pd.Series

  '''def col_type(self, value:datetime64):
    self.name = value.get('col_name')'''

  def get_name(self):
    """
    Return name of selected column
    """
    st.write(f'name of column: {self.col_name}')


    #return None

  def get_unique(self):
    """
    Return number of unique values for selected column
    """

    st.write(f"number of unique values {len(pd.unique(self.serie))}")
    #return None

  def get_missing(self):
    """
    Return number of missing values for selected column
    """
    st.write(f"number of missing values {self.serie.isna().sum()}")
    #return None

  def get_weekend(self):
    """
    Return number of occurrence of days falling during weekend (Saturday and Sunday)
    """
    st.write(f"number of weekend days {self.serie.dt.dayofweek.isin([5,6]).sum()}")
    #return None

  def get_weekday(self):
    """
    Return number of weekday days (not Saturday or Sunday)
    """
    st.write(f"number of weekday days {self.serie.dt.dayofweek.isin([0,1,2,3,4]).sum()}")
    #return None
  
  def get_future(self):
    """
    Return number of cases with future dates (after today)
    """
    st.write(f'''number of future days {sum ( self.serie > pd.to_datetime("today") )}''')
    #return None

  def get_empty_1900(self):
    """
    Return number of occurrence of 1900-01-01 value
    """
    num = 0
    for i in self.serie:
      if str(i).startswith('1900-01-01'):
        num+=1
    print (num) 
    
    return None

  def get_empty_1970(self):
    """
    Return number of occurrence of 1970-01-01 value
    """
    num = 0
    for i in self.serie:
      if str(i).startswith('1970-01-01'):
        num+=1
    print (num) 
    return None

  def get_min(self):
    """
    Return the minimum date
    """
    print (self.serie.min())
    #return None

  def get_max(self):
    """
    Return the maximum date 
    """
    print (self.serie.max())
    #return None

  def get_barchart(self):
    """
    Return the generated bar chart for selected column
    """
    
    print(self.serie.value_counts())
    
    #return None

  def get_frequent(self):
    """
    Return the Pandas dataframe containing the occurrences and percentage of the top 20 most frequent values
    """
    return None
