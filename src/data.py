import streamlit as st
from dataclasses import dataclass
import pandas as pd

def read_data(name, df):
    ls = Dataset(name, df)
    st.header('1. Overall Information')
    st.write(f'**Name of Table:** {ls.get_name()}')
    st.write(f'**Number of Rows:** {ls.get_n_rows()}')
    st.write(f'**Number of Columns:** {ls.get_n_cols()}')
    st.write(f'**Number of Duplicated Rows:** {ls.get_n_duplicates()}')
    st.write(f'**Number of Rows with Missing Values:** {ls.get_n_missing()}')
    st.write('**List of Columns:** ')
    st.text(', '.join(ls.get_cols_list()))
    st.write('**Types of Columns:**')
    st.dataframe(pd.DataFrame.from_dict(ls.get_cols_dtype(), orient='index', columns=(['type'])))
    show_nrows = st.slider('Select the number of rows to be displayed', 5, 50, 5)
    container1 = st.container()
    select_column = st.multiselect('Which columns do you want to convert to dates', ls.get_text_columns())
    with container1:
      try: 
        if any(col in select_column for col in df.columns):
          for i in select_column:
            df[i] = pd.to_datetime(df[i])
            df.append(df[i])
          st.write('**Top Rows of Table**', ls.get_head(show_nrows))
          st.write('**Bottom Rows of Table**', ls.get_tail(show_nrows))
          st.write('**Random Sample Rows of Table**', ls.get_sample(show_nrows))
        else:
          st.write('**Top Rows of Table**', ls.get_head(show_nrows))
          st.write('**Bottom Rows of Table**', ls.get_tail(show_nrows))
          st.write('**Random Sample Rows of Table**', ls.get_sample(show_nrows))
      except:
        st.write('**Top Rows of Table**', ls.get_head(show_nrows))
        st.write('**Bottom Rows of Table**', ls.get_tail(show_nrows))
        st.write('**Random Sample Rows of Table**', ls.get_sample(show_nrows))
        st.write(f'**_{i}_** cannot be converted into datetime')

@dataclass
class Dataset:
  name: str
  df: pd.DataFrame
  
  def get_name(self):
    """
    Return filename of loaded dataset
    """
    return self.name

  def get_n_rows(self):
    """
      Return number of rows of loaded dataset
    """
    return len(self.df)

  def get_n_cols(self):
    """
      Return number of columns of loaded dataset
    """
    return len(self.df.columns)

  def get_cols_list(self):
    """
      Return list column names of loaded dataset
    """
    return list(self.df.keys())

  def get_cols_dtype(self):
    """
      Return dictionary with column name as keys and data type as values
    """
    return self.df.dtypes.apply(lambda x: x.name).to_dict()

  def get_n_duplicates(self):
    """
      Return number of duplicated rows of loaded dataset
    """
    return self.df.duplicated().sum()

  def get_n_missing(self):
    """
      Return number of rows with missing values of loaded dataset
    """
    return self.df.isna().count()[1]

  def get_head(self, n=5):
    """
      Return Pandas Dataframe with top rows of loaded dataset
    """
    return self.df.head(n)

  def get_tail(self, n=5):
    """
      Return Pandas Dataframe with bottom rows of loaded dataset
    """
    return self.df.tail(n)

  def get_sample(self, n=5):
    """
      Return Pandas Dataframe with random sampled rows of loaded dataset
    """
    return self.df.sample(n)

  def get_numeric_columns(self):
    """
      Return list column names of numeric type from loaded dataset
    """
    return list(self.df.select_dtypes(include=['int64','float64']).columns)

  def get_text_columns(self):
    """
      Return list column names of text type from loaded dataset
    """
    return list(self.df.select_dtypes(include=['O']).columns)

  def get_date_columns(self):
    """
      Return list column names of datetime type from loaded dataset
    """
    return list(self.df.select_dtypes(include=['datetime64[ns]']).columns)

