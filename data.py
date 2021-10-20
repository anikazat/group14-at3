import streamlit as st
import pandas as pd

csv_file = st.file_uploader("Choose a CSV file")
if csv_file is not None:
    df = pd.read_csv(csv_file)

st.title('Overall Information')

st.write(f'**Name of Table:** {csv_file.name}')
st.write(f'**Number of Rows:** {len(df)}')
st.write(f'**Number of Columns:** {len(df.columns)}')
st.write(f'**Number of Duplicated Rows:** {print(df.duplicated)}')
st.write(f'**Number of Rows with Missing Values:** {sum(map(any, df.isna()))}')
st.write('**List of Columns:** ', ', '.join(list(df.keys())))
#add types of columns here
show_nrows = st.slider('Select the number of rows to be displayed', 5, 50, 5)
st.write('Top Rows of Table', df.head(show_nrows).to)
st.write('Bottom Rows of Table', df.tail(show_nrows))
st.write('Random Sample Rows of Table', df.sample(show_nrows))
#fix multiselect to convert dates
convert_date = st.multiselect('Which columns do you want to convert to dates?', df.columns)
