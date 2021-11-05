from dataclasses import dataclass
from pandas import Series,DataFrame
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


def read_numeric(n_data):
    column = n_data.columns
    n=0
    for i in column:
        if n_data[(f'{i}')].dtype == int or n_data[(f'{i}')].dtype == float:
          ls = NumericColumn((f'{i}'),pd.Series(n_data[(f'{i}')].values))
          st.subheader(f'2.{n} Field Name: {ls.col_name}')
          st.dataframe(ls.table())
          st.markdown(f'* Histogram')

          if ls.get_missing() == len(ls.serie):
             st.write(f'Can not create Histogram without values')
          else:
             st.pyplot(ls.get_histogram())

          st.markdown(f'* Most Frequent Values')
          if ls.get_missing() == len(ls.serie):
            st.markdown("No frequent values")
          else:
            st.dataframe(ls.frequent().head(20))
          n=n+1

        else:pass
        #get result from NumericColumn,and organize the display structure

@dataclass
class NumericColumn:
  col_name: str
  serie: pd.Series

  def get_name(self):
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


   
  def get_histogram(self):
    fig, ax = plt.subplots()
    ax.hist(self.serie, bins=50,edgecolor='white')
    plt.xlabel(f'{self.col_name}')
    plt.ylabel('Count of Records')
    return fig
  
  def frequent(self):
    do=self.serie.value_counts(ascending=False)
    dt=self.serie.value_counts(normalize=True)
    table={'value':do.index,
            'occur':do.values,
            'freq':dt.values}
    dc=pd.DataFrame(table)
    return dc


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

   