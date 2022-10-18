import streamlit as st
import pandas as pd

st.title('Deploy testing')

selectStartDate = st.date_input('Starting date..')

if selectStartDate:
    st.write(selectStartDate)

st.write('Oppdatert')

data = pd.DataFrame()

pdFile = st.file_uploader('Upload .csv', type='csv')

if pdFile:
    data = pd.read_csv(pdFile, decimal=",", sep=";")

st.dataframe(data)