import streamlit as st
from dataclasses import dataclass
import pandas as pd

csv_file = st.file_uploader("Choose a CSV file")
if csv_file is not None:
    df = pd.read_csv(csv_file)
else:
    st.write('No csv file uploaded')

@dataclass
class Dataset:
  name: str
  df: pd.DataFrame
  
  def get_name(self):
    """
    Return filename of loaded dataset
    """
    self.name = csv_file.name
    return self.name

  def get_n_rows(self):
    """
      Return number of rows of loaded dataset
    """
    self.df = df
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
    return ', '.join(list(self.df.keys()))

  def get_cols_dtype(self):
    """
      Return dictionary with column name as keys and data type as values
    """
    return dict(self.df.dtypes)

  def get_n_duplicates(self):
    """
      Return number of duplicated rows of loaded dataset
    """
    return df.duplicated

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
    return ', '.join(list(self.df.select_dtypes(include=['int64','float64']).columns))

  def get_text_columns(self):
    """
      Return list column names of text type from loaded dataset
    """
    return ', '.join(list(self.df.select_dtypes(include=['O']).columns))

  def get_date_columns(self):
    """
      Return list column names of datetime type from loaded dataset
    """
    return ', '.join(list(self.df.select_dtypes(include=['datetime64[ns]']).columns))


def datetime_fun(column):
    """ 
    function that will convert a colomn to datetime format
    """
    df[column] = pd.to_datetime(df[column], format='%Y-%m-%d %H:%M:%S')
    return(df)

def form_callback():
    #st.write(st.session_state.select_column)
    st.session_state.select_column = select_column

st.title('Overall Information')
st.write(f'**Name of Table:** {Dataset.get_name(Dataset)}')
st.write(f'**Number of Rows:** {Dataset.get_n_rows(df)}')
st.write(f'**Number of Columns:** {Dataset.get_n_cols(df)}')
st.write(f'**Number of Duplicated Rows:** {print(Dataset.get_n_duplicates(df))}')
st.write(f'**Number of Rows with Missing Values:** {Dataset.get_n_missing(df)}')
st.write(f'**List of Columns:** {Dataset.get_cols_list(df)}')
st.write('**Types of Columns:**', Dataset.get_cols_dtype(df))
show_nrows = st.slider('Select the number of rows to be displayed', 5, 50, 5)
select_column = st.multiselect('Which columns do you want to convert to dates', df.select_dtypes(include='object').columns, on_change=form_callback)

if any(ele in select_column for ele in df.columns):
    for i in select_column:
        x = datetime_fun(i)
        df.append(x)
    st.write('Top Rows of Table', Dataset.get_head(df, show_nrows))
    st.write('Bottom Rows of Table', Dataset.get_tail(df, show_nrows))
    st.write('Random Sample Rows of Table', Dataset.get_sample(df, show_nrows))
else:
    st.write('Top Rows of Table', Dataset.get_head(df, show_nrows))
    st.write('Bottom Rows of Table', Dataset.get_tail(df, show_nrows))
    st.write('Random Sample Rows of Table', Dataset.get_sample(df, show_nrows))

