import pandas as pd
import streamlit as st
# from data import df
from dataclasses import dataclass
from pandas import Series,DataFrame
from streamlit.delta_generator import DELTA_TYPES_THAT_MELT_DATAFRAMES

st.title('Numeric Information')

@dataclass
class NumericColumn:
  col_name: str
  serie: pd.Series
  def get_name(self):
    if self.serie.values.dtype != object:
      return self.col_name
 
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
    return data

  
DELTA_TYPES_THAT_MELT_DATAFRAMES
