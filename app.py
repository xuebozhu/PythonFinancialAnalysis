import streamlit as st
import pandas as pd

from prediction import load_data, train_arima, forecast

st.title('IBEX35 Forecast Dashboard')

uploaded_file = st.file_uploader('Upload IBEX35 CSV file', type='csv')
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    df['Date'] = pd.to_datetime(df['<DTYYYYMMDD>'].astype(str), format='%Y%m%d')
    df = df.set_index('Date').sort_index()

    df['MA20'] = df['<CLOSE>'].rolling(window=20).mean()
    df['MA50'] = df['<CLOSE>'].rolling(window=50).mean()

    st.subheader('Recent Data')
    st.dataframe(df.tail())

    st.subheader('Closing Price and Moving Averages')
    st.line_chart(df[['<CLOSE>', 'MA20', 'MA50']].dropna())

    days = st.slider('Days to forecast', 1, 30, 5)
    if st.button('Run Forecast'):
        model = train_arima(df)
        pred = forecast(model, days)
        st.subheader('Forecasted Close Prices')
        st.line_chart(pred)
else:
    st.info('Please upload a CSV file to begin.')
