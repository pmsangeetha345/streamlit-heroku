import streamlit as st
import pandas as pd
from sklearn import datasets
from sklearn.ensemble import RandomForestClassifier
import pickle

st.write("""
# Check if the given number is Odd or Even

This app predicts if the provided number is odd or even
""")
#Get Input

st.header('User Input Parameters')
inp_number = 0
def user_input_features():
    inp_number = st.number_input("inp_number")
    if (inp_number % 2) == 0:
      out_val = 'The given number is Even'
    else:
      out_val = 'The given number is Odd'
   
    st.header(out_val)

user_input_features()