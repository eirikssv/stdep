import streamlit as st
import pandas as pd

st.title('Deploy testing')

selectStartDate = st.date_input('Starting date..')

if selectStartDate:
    st.write(selectStartDate)
    