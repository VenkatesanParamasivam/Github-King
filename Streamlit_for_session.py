# -*- coding: utf-8 -*-
"""
Created on Tue Nov 16 08:23:22 2021

@author: Venkatesan
"""

import streamlit as st
import pandas as pd

st.title("Data Science with Python")
# st.text_area("Enter you sentences")

data_file=st.file_uploader("uploaded file",type=["csv","excel"])
if st.button("Submit"):
    data=pd.read_csv(data_file)
    st.line_chart(data)
