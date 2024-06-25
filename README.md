# Particulate Matter Prediction Using Time Series
Link of Google Colab notebook: https://colab.research.google.com/drive/1Frnd2tQHLUbRwPdKpxXAe4X7NrJ7G5et?usp=sharing   
Deployed this app in Streamlit Cloud: https://pm-prediction.streamlit.app/
## Problem Statement
Air pollution, specifically particulate matter (PM), poses significant health risks and environmental challenges. Predicting future PM levels can aid in mitigating these risks by enabling proactive measures. This project aims to develop a robust time series model to accurately forecast PM concentrations (PM2.5 and PM10) using historical data, thereby providing valuable insights for policy-makers, researchers, and the general public to improve air quality management and public health outcomes.
## Dataset Description
Dataset has been recorded from January 1, 2018 till December 31, 2023. 
No. of rows = 52,450, 
No. of columns = 11
1. YEAR
2. MO (Month)
3. DY (Day)
4. HR (Hour)
5. T2M (Temperature at 2 meters)
6. RH2M (Relative Humidity at 2 meters)
7. PRECTOTCORR (Corrected Total Precipitation)
8. WS10M (Wind Speed at 10 meters)
9. WD10M (Wind Direction at 10 meters)
10. PM2.5
11. PM10
## Installation
To run the code in this repository, you need to have Python (version 3.9.13 recommended) installed. You can install the required packages using:

```bashfrequency 
pip install -r requirements.txt
```
## Data Preprocessing
1. Since the dataset contains separate values of YEAR, MO, DY and HR, we need to first create a new column 'Date' which contain the values of columns 'YEAR', 'MO', 'DY', 'HR' and convert it into datetime format.
2. Set 'Date' column as index for the dataset.
3. Remove 'YEAR', 'MO', 'DY', 'HR' columns from the dataset to avoid redundancy.
4. Remove the null values from the dataset.
5. As our dataset contains hourly information of particulate matter data, we need to set frequency of our dataset as 'H'.
### Note: Detailed code has been provided in `PM_prediction.ipynb`

## Models Trained
Since we need to predict PM2.5 and PM10 from external environmental factors, our model should be a multi-label regression model. The models have been trained for predicting both PM2.5 and PM10 values. The dataset has been trained upon a number of models:
1. Linear Regression
2. ARIMAX (ARIMA with exogenous variables)
3. VAR (Vector Auto Regression)
4. Random Forest
5. LSTM (Long Short Term Memory)
6. FB Prophet
## Results
### From all the models mentioned above, our best performing model is LSTM.



