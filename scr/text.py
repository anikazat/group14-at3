import streamlit as st
from dataclasses import dataclass
import pandas as pd
from pandas import Series
from scr.text import TextColumn


st.subheader('Information on text columns')

'''csv_file = st.file_uploader("Choose a CSV file", type=['csv'])
df = pd.read_csv(csv_file)'''

'''ile_url = ('https://github.com/CSSEGISandData/COVID-19/blob/master/csse_covid_19_data/csse_covid_19_daily_reports_us/01-01-2021.csv?raw=true')
df = pd.read_csv(file_url)
newdf = df.select_dtypes(include=object)'''

'''
if st.checkbox('Show data'):
     st.write(df)'''

def rd_text(n_data):
    column = n_data.columns
    for i in column:
        if n_data[(f'{i}')].dtype == object
            # print('no')
        else:
            ls = TextColumn((f'{i}'),pd.Series(n_data[(f'{i}')].values))
            # subtitle=ls.get_name()
            ls.table()
            ls.freq()


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

  def get_barchart(self):
    occurrence = self.serie.value_counts()
    value = df.self.serie 
    barchart = self.serie.plot.bar(x=value, y=occurrence, rot=0)
    return barchart

  def get_frequent(self):
      Frequency_percentage = self.serie.apply(pd.value_counts)
      return Frequency_percentage 


st.write(f'**3.3 Field Name:** {TextColumn.get_name(TextColumn)}')
st.write(f'**Number of Unique Values:** {get_unique(serie)}')
st.write(f'**Number of Missing Values:** {self.serie.isna().sum()}')
st.write(f'**Number of Missing Values:** {self.serie.isna().sum()}')

st.write(f'**Number of Rows with Empty String:** {(self.serie.values == '').sum()}') 

st.write(f'**Number of Rows with Only Whitespaces:** {self.serie.values == ' ').sum()}

st.write(f'**Number of Rows with Only Lower Case Characters:** {self.serie.str.count(str.islower = True)}

st.write(f'**Number of Rows with Only Upper Case Characters:** {self.serie.str.count(str.isupper = True)}

st.write(f'**Number of Rows with Only Alphabet Characters:** {self.serie.count(series.str.isalpha = TRUE)}

st.write(f'**Number of Rows with Only Number as Characters:** {self.serie.count(series.str.isnumeric = TRUE)}

st.write(f'**Mode for Selected Column:** {self.serie.mode()}

# st.write(f'*Number of Occurrence for Each Value:** {bar_chart(self.serie.value_counts())}

# st.write(f'**Frequencies and Percentage for Each Value:** {}
