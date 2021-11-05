# To be filled by students
#from numpy import datetime64
import streamlit as st
from dataclasses import dataclass
import pandas as pd
from pandas import Series,DataFrame
import datetime



def rd_dtime(datetype):
  column = datetype.columns
  n=0
  for i in column:
    
    
    if datetype[(f'{i}')].dtype == int or datetype[(f'{i}')].dtype == float or datetype[(f'{i}')].dtype == object:pass
    # tried to use  .dtype = datetime or datetime64 directly,but it doesn't work( to recognise datetime datatype columns)
    # therefore, here set the condition to filter out numeric types and text types
    
    else:
      dt = DateColumn((f'{i}'),pd.Series(datetype[(f'{i}')].values))
      st.subheader(f'4.{n} Field Name:{dt.get_name()}')
      #st.dataframe(dt.table())
      st.markdown(f'Bar Chart')
      #st.write(dt.get_barchart())
      st.markdown(f'Most Frequent Values')
      st.write(dt.get_frequent())
      
      n=n+1



@dataclass
class DateColumn:
  col_name: str
  serie: pd.Series

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
    unique = self.serie.nunique()
    return unique

    #return len(pd.unique(self.serie))
    

  def get_missing(self):
    """
    Return number of missing values for selected column
    """
    missing = self.serie.isna().sum()
    return missing

  def get_weekend(self):
    """
    Return number of occurrence of days falling during weekend (Saturday and Sunday)
    """
    
    weekend = self.serie.dt.dayofweek.isin([5,6]).sum()
    return weekend

  def get_weekday(self):
    """
    Return number of weekday days (not Saturday or Sunday)
    """
    weekday = self.serie.dt.dayofweek.isin([0,1,2,3,4]).sum()
    return weekday
  
  def get_future(self):
    """
    Return number of cases with future dates (after today)
    """
    
    future = sum ( self.serie > pd.to_datetime("today") )
    return future

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
        
    return num

  def get_min(self):
    """
    Return the minimum date
    """
    min = self.serie.min()
    return min

  def get_max(self):
    """
    Return the maximum date 
    """
    
    max = self.serie.max()
    return max

  def get_barchart(self):
    """
    Return the generated bar chart for selected column
    """
    
    return st.bar_chart(self.serie.value_counts())
    
  
  def get_frequent(self):

    """
    Return the Pandas dataframe containing the occurrences and percentage of the top 20 most frequent values
    """
    dat=self.serie.value_counts(ascending=False)
    dp=self.serie.value_counts(normalize=True)
    table={'value':dat.index,
           'occurence':dat.values,
           'percentage':dp.values}
    dfr=DataFrame(table)
    return dfr.head(20)
  
  
  
  def table(self):
    date_data={'value':{'Number of Unique Values':self.get_unique(), 
                    'Number of Rows with Missing Values':self.get_missing(),
                    'Number of Weekend Dates':self.get_weekend(),
                    'Number of Weekday Dates':self.get_weekday(),
                    'Number of Dates in Future':self.get_future(),
                    'Number of Rows with 1900-01-01':self.get_empty_1900(),
                    'Number of Rows with 1970-01-01':self.get_empty_1970(),
                    'Minimun Value':self.get_min(),
                    'Maximun Value':self.get_max()}}
    data=DataFrame(date_data)
    return data
