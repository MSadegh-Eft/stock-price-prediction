# uncomment the pickle !!!!!!!!!!!!!!!

import datetime, pickle # for saving data, for example the classification
import streamlit         as st
import numpy             as np
import yfinance          as yf
import matplotlib.pyplot as plt #for graphing
from sklearn                 import preprocessing, svm
from sklearn.linear_model    import LinearRegression
from sklearn.model_selection import train_test_split

###################### FOOTER

footer="""<style>
a:link , a:visited{
color: blue;
background-color: transparent;
text-decoration: underline;
}

a:hover,  a:active {
color: red;
background-color: transparent;
text-decoration: underline;
}

.footer {
position: fixed;
left: 0;
bottom: 0;
width: 100%;
background-color: white;
color: black;
text-align: center;
}
</style>
<div class="footer">
<p>Developed by <a style='display: block; text-align: center;' href="https://github.com/nosadeghob" target="_blank">Mohammad sadegh Eftekhar</a></p>
</div>
"""
st.markdown(footer,unsafe_allow_html=True)

#######################################

st.markdown("<h1 style='text-align: center; color: white;'>Stock Price Prediction</h1>", unsafe_allow_html=True)
st.set_option('deprecation.showPyplotGlobalUse', False)
#st.title('Stock Price Prediction')
plt.figure(figsize=(12, 6))

with st.sidebar:
    user_input = st.text_input('Enter Stock Ticker', 'AAPL')
    #user_start_date = st.text_input('Enter Start Date', '2010-01-01')
    #user_end_date = st.text_input('Enter end Date', '2022-01-01')
    user_start_date = st.date_input('Enter Start Date',datetime.date(2010, 1, 1))
    user_end_date = st.date_input('Enter end Date', datetime.date(2022, 12, 31))
    #prediction_days = st.number_input('Enter The Number Of Prediction Days')
    prediction_days = st.slider('Enter The Number Of Prediction Days', 1, 30, 10)

if user_start_date>user_end_date:
    # st.sidebar.write(":red[Error: the start date can't be after the end date !!!]")
