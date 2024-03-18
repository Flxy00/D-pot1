import streamlit as st
import pandas as pd
import numpy as np

voc=pd.read_CSV('https://docs.google.com/spreadsheets/d/e/2PACX-1vST1KuuolQSsMjI6Xemgo6a1CD5ys4RGhOYDntzJh-JylhPF2C7_D0ecpQFRTkhhhV-SVyC22-beYBd/pub?gid=0&single=true&output=csv')
st.dataframe(voc)
l=voc.shape[0]
i=np.random.choice(range(l))
word_fr= voc['Définition'].values[i]
word_chi= voc['Hanzi'].values[i]
st.write(word_fr+""+ word_chi)
