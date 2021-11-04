import pandas as pd
import streamlit as st
from dataclasses import dataclass
from pandas import Series,DataFrame


st.subheader('Information on text columns')

'''csv_file = st.file_uploader("Choose a CSV file", type=['csv'])
df = pd.read_csv(csv_file)'''

'''file_url = ('https://github.com/CSSEGISandData/COVID-19/blob/master/csse_covid_19_data/csse_covid_19_daily_reports_us/01-01-2021.csv?raw=true')
df = pd.read_csv(file_url)
newdf = df.select_dtypes(include=object)'''



def rd_text(o_data):
    column = o_data.columns
    for i in column:
        if o_data[(f'{i}')].dtype == object:
          dt = TextColumn((f'{i}'),pd.Series(o_data[(f'{i}')].values))
          dt.table()
          dt.get_barchart()
          dt.get_frequent()
            
        else:
            return None


@dataclass
class TextColumn:
  col_name: str
  serie: pd.Series

  def get_name(self):
    if self.serie.values.dtype == object:
      return self.col_name

  def get_unique(self):
    unique_values = len(self.serie.unique())
    return unique_values

  def get_missing(self):
    missing_values = self.serie.isna().sum()
    return missing_values

  def get_empty(self):
    empty_string = (self.serie.values == '').sum()
    return empty_string

  def get_whitespace(self):
    white_spaces = (self.serie.values == ' ').sum()
    return white_spaces 

  def get_lowercase(self):
    lower_case_characters = self.serie.str.count(str.islower == True)
    return lower_case_characters 

  def get_uppercase(self):
    upper_case_characters = self.serie.str.count(str.isupper == True)
    return upper_case_characters

  def get_alphabet(self):
    alphabet_characters = self.serie.count(series.str.isalpha == True)
    return alphabet_characters  
 
  def get_digit(self):
    numbers_as_characters = self.serie.count(series.str.isnumeric == True)
    return numbers_as_characters

  def get_mode(self):
    mode_value = self.serie.mode()
    return mode_value 

 

  def table(self):
    test_data={'value':{'number of unique values':self.get_unique(),
    'number of missing values': self.get_missing(),
    'number of empty rows': self.get_empty(),
    'number of whitespace rows':self.get_whitespace(),
    'number of lower case rows': self.get_lowercase(),
    'number of upper case rows': self.get_uppercase(),
    'number of alphabet rows': self.get_alphabet(),
    'number of digit rows': self.get_digit(),
    'Mode for selected column': self.get_mode(),
    'number of occurrence': self.get_barchart(),
    'number of frequency': self.get_frequent()}} 
    data=DataFrame(test_data)
    return data 

  def get_barchart(self):
    occurrence = self.serie.value_counts()
    value = df.self.serie 
    barchart = self.serie.plot.bar(x=value, y=occurrence, rot=0)
    return barchart


  def get_frequent(self):
        if self.get_missing() == len(self.serie):pass
        else:
            do=self.serie.value_counts(ascending=False)
            dt=self.serie.value_counts(normalize=True)
            table={'value':do.index,
                  'occur':do.values,
                  'freq':dt.values}
            dc=DataFrame(table)
st.markdown(f'* Most Frequent Values'),st.write(dc.head(20))

 
st.write(f'**3.3 Field Name:** {TextColumn.get_name(TextColumn)}')
st.write(f'**Number of Unique Values:** {TextColumn.get_unique()}')

st.write(f'**Number of Missing Values:** {TextColumn.get_missing()}') 

st.write(f'**Number of Missing Values:** {TextColumn.get_missing()}')

st.write(f'**Number of Rows with Empty String:** {(TextColumn.get_empty())}') 

st.write(f'**Number of Rows with Only Whitespaces:** {TextColumn.get_whitespace()}')

st.write(f'**Number of Rows with Only Lower Case Characters:** {TextColumn.get_lowercase()}')

st.write(f'**Number of Rows with Only Upper Case Characters:** {TextColumn.get_uppercase()}')

st.write(f'**Number of Rows with Only Alphabet Characters:** {TextColumn.get_alphabet()}')

st.write(f'**Number of Rows with Only Number as Characters:** {TextColumn.get_digit()}')

st.write(f'**Mode for Selected Column:** {TextColumn.get_mode()}')

st.write(f'*Number of Occurrence for Each Value:** {TextColumn.get_barchart()}')

st.write(f'**Frequencies and Percentage for Each Value:** {TextColumn.get_frequent()}')

