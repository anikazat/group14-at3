from dataclasses import dataclass
from numpy import NaN
from pandas import Series,DataFrame
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


def rd_numeric(n_data):
    column = n_data.columns
    n=0
    for i in column:
        if n_data[(f'{i}')].dtype == object:pass
        
        else:
          ls = NumericColumn((f'{i}'),pd.Series(n_data[(f'{i}')].values))
          st.subheader(f'2.{n} Field Name: {i}')
          ls.table()
          ls.get_histogram()
          ls.freq()
          n=n+1
            
@dataclass
class NumericColumn:
  col_name: str
  serie: pd.Series
  def get_name(self):
    # if self.serie.values.dtype != object:
    return self.col_name
    # else:pass
 
  def get_unique(self):
    unique=self.serie.value_counts().sum()
    return unique
  
  def get_missing(self):
    miss=self.serie.isnull().sum()
    return miss
  
  def get_zeros(self):
    zero= (self.serie.values == 0).sum()
    return zero
  
  def get_negatives(self):
    neg= (self.serie.values <0).sum()
    return neg

  def get_mean(self):
    mean= self.serie.mean()
    return mean
  
  def get_std(self):
    std= self.serie.std()
    return std
  
  def get_min(self):
    min= self.serie.min()
    return min
  
  def get_max(self):
    max= self.serie.max()
    return max
  
  def get_median(self):
    mid= self.serie.median()
    return mid

  def table(self):
    test_data={'value':{'number of unique values':self.get_unique(), 
                    'number of missing values':self.get_missing(),
                    'number of occurrence of 0 value':self.get_zeros(),
                    'number of negative values':self.get_negatives(),
                    'average value':self.get_mean(),
                    'standard deviation value':self.get_std(),
                    'minimum value':self.get_min(),
                    'maximum value':self.get_max(),
                    'median value':self.get_median()}}
    data=DataFrame(test_data)
    return st.write(data)
  
  def get_histogram(self):
    if self.get_missing() == len(self.serie):
      st.markdown(f'* Can not create Histogram without values')
    else:
      fig, ax = plt.subplots()
      ax.hist(self.serie, bins=50,edgecolor='white')
      plt.xlabel(f'{self.col_name}')
      plt.ylabel('Count of Records')
      st.markdown(f'* Histogram'),st.pyplot(fig)
  
  def freq(self):
    if self.get_missing() == len(self.serie):pass
    else:
      do=self.serie.value_counts(ascending=False)
      dt=self.serie.value_counts(normalize=True)
      table={'value':do.index,
            'occur':do.values,
            'freq':dt.values}
      dc=DataFrame(table)
      st.markdown(f'* Most Frequent Values'),st.write(dc.head(20))
