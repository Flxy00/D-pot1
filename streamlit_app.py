import streamlit as st
import pandas as pd
import numpy as np
voc=pd.read_CSV('https://docs.google.com/spreadsheets/d/1jH6kJJISFA0Ye4gE4CzG7ZEjBJhCRelGOZN-HnxyZBQ/edit')
st.dataframe(voc)
l= voc.shape[0]
i= np.random.choice(range(l))
word_fr= voc['Définition'].values[i]
word_chi= voc['Hanzi'].values[i]
st.write(word_fr+""+ word_chi)
