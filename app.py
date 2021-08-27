from requests.exceptions import RequestsWarning
import streamlit as st
import datetime
import pandas as pd
import requests

st.markdown('''
# Prediction of the NY Taxi Fare

Select the parameters provided below:
''')

if st.checkbox('Do you want to make a prediction?'):

    date = st.date_input("Select the date:", datetime.date(2021, 8, 27))

    time = st.time_input('Select the time:', datetime.time(8, 45))

    pickup_longitude = st.number_input('Insert the pickup longitude')

    pickup_latitude = st.number_input('Insert the pickup latitude')

    dropoff_longitude = st.number_input('Insert the dropoff longitude')

    dropoff_latitude = st.number_input('Insert the dropoff latitude')

    passenger_count = st.number_input('Insert the passenger count')

    url = 'https://taxifare.lewagon.ai/predict'

    dictionary_param = {
        'key': '2013-07-06 17:18:00.000000119',
        'pickup_datetime': str(date) + ' ' +str(time),
        'pickup_longitude': float(pickup_longitude),
        'pickup_latitude': float(pickup_latitude),
        'dropoff_longitude': float(dropoff_longitude),
        'dropoff_latitude': float(dropoff_latitude),
        'passenger_count': int(passenger_count)
    }

    response = requests.get(url, params=dictionary_param).json()

    if st.button('Get Prediction'):
        # print is visible in the server output, not in the page
        print('button clicked!')
        st.write(response)
    else:
        st.write('Click on the button to find out how much the fare will be!')
