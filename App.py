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
    st.sidebar.markdown(f'<h1 style="background-color:#FFFFFF;text-align: center;color:#C34104;font-size:24px;">Error: the start date cant be after the end date !!!</h1>', unsafe_allow_html=True)

else:
    df = yf.download(user_input, user_start_date, user_end_date)

# describing data
subheader_output = 'Raw Dataframe from ' + str(user_start_date.year) + '-' + str(user_end_date.year) +' ('+ str(df.shape[0]) + ' Days)'
st.subheader(subheader_output) # used a variable because it cant handle more than 3 inputs
st.write(df)
#st.table(df)
#print(df.shape)

#visualizations
st.subheader('Closing price')
plt.title(user_input) #***************
plt.xlabel('Days')
plt.ylabel('Close Price')
plt.plot(df['Adj Close'], 'b')
#plt.show()
st.pyplot()

##############################################################

df = df.drop(['Close'], axis=1)

df['HL_PCT'] = (df['High'] - df['Low']) / df['Adj Close'] * 100.0 #PCT means percent 
# the "HL_PCT" is supposted to be "high - low"

df['PCT_CHANGE'] = (df['Adj Close'] - df['Open']) / df['Open'] * 100.0 # we multipliy it just to make it smaller
df = df[['Adj Close', 'HL_PCT', 'PCT_CHANGE', 'Volume']]

# describing data
subheader_output = 'New Dataframe from ' + str(user_start_date.year) + '-' + str(user_end_date.year)
st.subheader(subheader_output) # used a variable because it cant handle more than 3 inputs
st.write(df)

#visualizations
st.subheader('PCT_CHANGE & HL_PCT')
title = user_input + '(PCT_CHANGE & HL_PCT)'
plt.title(title) #***************
plt.xlabel('Days')
plt.ylabel('Close Price')
plt.plot(df['PCT_CHANGE'])
plt.plot(df['HL_PCT'], 'r')
plt.legend(["PCT_CHANGE", "HL_PCT"], loc ="lower right") # show the guide on the corner
#plt.show()
st.pyplot()

###################################

st.subheader('Closing Price vs Time chart with 100MA & 200MA') # 'MA' : mean average
ma100 = df['Adj Close'].rolling(100).mean()
