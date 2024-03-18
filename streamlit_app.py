import streamlit as st
import pandas as pd

voc=pd.read_CSV ('https://docs.google.com/spreadsheets/d/e/2PACX-1vST1KuuolQSsMjI6Xemgo6a1CD5ys4RGhOYDntzJh-JylhPF2C7_D0ecpQFRTkhhhV-SVyC22-beYBd/pub?output=csv')
st.dataframe(voc)
