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
    self.name = self.col_name
    
    return self.name

  def get_unique(self):
    """
    Return number of unique values for selected column
    """
    
    return len(pd.unique(self.serie))

  def get_missing(self):
    """
    Return number of missing values for selected column
    """
    return self.serie.isna().sum()

  def get_weekend(self):
    """
    Return number of occurrence of days falling during weekend (Saturday and Sunday)
    """
    return self.serie.dt.dayofweek.isin([5,6]).sum()

  def get_weekday(self):
    """
    Return number of weekday days (not Saturday or Sunday)
    """
    return self.serie.dt.dayofweek.isin([0,1,2,3,4]).sum()
  
  def get_future(self):
    """
    Return number of cases with future dates (after today)
    """
    return sum ( self.serie > pd.to_datetime("today") )

  def get_empty_1900(self):
    """
    Return number of occurrence of 1900-01-01 value
    """
    num = 0
    for i in self.serie:
      if str(i).startswith('1900-01-01'):
        num+=1
        
    return num

  def get_empty_1970(self):
    """
    Return number of occurrence of 1970-01-01 value
    """
    num = 0
    for i in self.serie:
      if str(i).startswith('1970-01-01'):
        num+=1
        
    return None

  def get_min(self):
    """
    Return the minimum date
    """
    return self.serie.min()

  def get_max(self):
    """
    Return the maximum date 
    """
    return self.serie.max() 

  def get_barchart(self):
    """
    Return the generated bar chart for selected column
    """
    
    return st.bar_chart(self.serie.value_counts())

  def get_frequent(self):
    """
    Return the Pandas dataframe containing the occurrences and percentage of the top 20 most frequent values
    """
    
    dat = self.serie.value_counts()
    dat = pd.DataFrame(dat)
    dat['occurence'] = self.serie.value_counts()
    dat['percentage'] = self.serie.value_counts(normalize=True)
    subset_cols = ['occurence','percentage']

    return dat[subset_cols].head(20)
