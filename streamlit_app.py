import streamlit as st
import pandas as pd
voc=pd.read_CSV('https://docs.google.com/spreadsheets/d/1ZVqjn50wq2PFTtrWIr_Dc8mfuJfHJUFcmRNjtA2LSv0/edit?usp=sharing')
st.dataframe(voc)
