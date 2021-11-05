import pandas as pd
import streamlit as st
from dataclasses import dataclass
from pandas import Series,DataFrame

def read_text(n_data):
    column = n_data.columns
    n=0
    for i in column:
        if n_data[(f'{i}')].dtype == int or n_data[(f'{i}')].dtype == object:
          ls = TextColumn((f'{i}'),pd.Series(n_data[(f'{i}')].values))
          st.subheader(f'3.{n} Field Name: {ls.col_name}')
          st.dataframe(ls.table())
          st.markdown(f'* Bar Chart')

          if ls.get_missing() == len(ls.serie):
             st.write(f'Can not create Bar_chart without values')
          else:
             st.pyplot(ls.get_barchart())

          st.markdown(f'* Most Frequent Values')
          if ls.get_missing() == len(ls.serie):
            st.markdown("No frequent values")
          else:
            st.dataframe(ls.frequent().head(20))
          n=n+1

        else:pass

@dataclass
class TextColumn:
  col_name: str
  serie: pd.Series

  def __init__(self, data):
    self.data = data
   

  def get_name(self):
    if self.data.dtypes == 'object':
      return self.data.name

  def get_unique(self):
    unique_values = len(self.data.unique())
    return unique_values
  
  def get_missing(self):
    missing_values = self.data.isna().sum()
    return missing_values

  def get_empty(self):
    empty_string = (self.data == '').sum()
    return empty_string

  def get_whitespace(self):
    white_spaces = (self.data == ' ').sum()
    return white_spaces 

  def get_lowercase(self):
    lower_case_characters =0
    for i in self.data:
      if i.islower():
        lower_case_characters +=1
    return lower_case_characters

  def get_uppercase(self):
    upper_case_characters =0
    for i in self.data:
      if i.isupper():
        upper_case_characters +=1
    return upper_case_characters

  def get_alphabet(self):
    alphabet_characters =0
    for i in self.data:
      if i.isalpha():
        alphabet_characters +=1
    return alphabet_characters  
 
  def get_digit(self):
    numbers_as_characters =0
    for i in self.data:
      if i.isnumeric():
        numbers_as_characters +=1
    return numbers_as_characters

  def get_mode(self):
    mode_value = self.data.mode()[0]
    return mode_value 

  def get_barchart(self):
    barchart = self.data.value_counts()
    return barchart

  def get_frequent(self):
      Frequency_percentage = self.data.value_counts()/len(self.data)
      occurence = self.data.value_counts()
      u=pd.concat([occurence,Frequency_percentage],axis = 1,keys =['Occurence','Frequency_percentage'])
      return u
 


def main():
  html_temp ="""
  <div style ="">
  <h1 style ="color:black;text-align:center;"> </h1>
  </div>
  """

  st.markdown(html_temp,unsafe_allow_html = True)
  uploaded_file = st.file_uploader("Choose a file")
  if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write(df)
    Field = st.selectbox('Field Name',(df.columns))
    name = Field
    s = pd.Series(df[name].values)
    
    t =TextColumn(s)

    test_data={'Value':{'number of unique values':t.get_unique(),
    'number of missing values': t.get_missing(),
    'number of empty rows': t.get_empty(),
    'number of whitespace rows':t.get_whitespace(),
    'number of lower case rows': t.get_lowercase(),
    'number of upper case rows': t.get_uppercase(),
    'number of alphabet rows': t.get_alphabet(),
    'number of digit rows': t.get_digit(),
    'Mode for selected column': t.get_mode()}}

    full=DataFrame(test_data)
    table1=full.astype(str)
    st.subheader("Exploratory Data Analysis")
    st.dataframe(table1)

    st.subheader("Bar Chart")
    st.bar_chart(t.get_barchart())

    st.subheader("Most Frequent Values")
    table2 = t.get_frequent()
    freq_table = table2.astype(str)
    st.dataframe(freq_table)


if __name__=='__main__': 
    main()
