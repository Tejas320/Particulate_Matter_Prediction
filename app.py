import streamlit as st
import pandas as pd
import numpy as np
import tensorflow as tf
from datetime import datetime

import os
os.environ["CUDA_VISIBLE_DEVICES"] = "-1"

tf.config.set_visible_devices([], 'GPU')

# Load the saved LSTM model
model = tf.keras.models.load_model('lstm_model.h5')

# Define the Streamlit UI
st.title('PM2.5 and PM10 Prediction')

# Create input fields for user input using Streamlit form
with st.form("prediction_form"):
    year = st.number_input('Year', min_value=2000, max_value=2100, step=1)
    month = st.number_input('Month', min_value=1, max_value=12, step=1)
    day = st.number_input('Day', min_value=1, max_value=31, step=1)
    hour = st.number_input('Hour', min_value=0, max_value=23, step=1)
    t2m = st.number_input('Temperature at 2 meters (T2M)')
    rh2m = st.number_input('Relative Humidity at 2 meters (RH2M)')
    ws10m = st.number_input('Wind Speed at 10 meters (WS10M)')
    wd10m = st.number_input('Wind Direction at 10 meters (WD10M)')
    prectotcorr = st.number_input('Total Precipitation (PRECTOTCORR)')
    
    submitted = st.form_submit_button("Predict")

    if submitted:
        # Create a DataFrame for the input data
        input_data = pd.DataFrame({
            'T2M': [t2m],
            'RH2M': [rh2m],
            'WS10M': [ws10m],
            'WD10M': [wd10m],
            'PRECTOTCORR': [prectotcorr]
        })
 
        # Reshape the input data to match the model input shape
        input_data = np.reshape(input_data.values, (input_data.shape[0], 1, input_data.shape[1]))

        # Make predictions
        prediction = model.predict(input_data)

        # Extract the predicted values
        pm25_prediction = prediction[0][0]
        pm10_prediction = prediction[0][1]

        # Display the prediction results
        st.write('### Prediction Result')
        st.write(f'Date and Time: {datetime(year, month, day, hour)}')
        st.write(f'Predicted PM2.5: {pm25_prediction:.2f}')
        st.write(f'Predicted PM10: {pm10_prediction:.2f}')