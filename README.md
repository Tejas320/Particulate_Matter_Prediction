# Particulate Matter Prediction Using Time Series
Link of Google Colab notebook: https://colab.research.google.com/drive/1Frnd2tQHLUbRwPdKpxXAe4X7NrJ7G5et?usp=sharing   
Deployed the app in Streamlit Cloud: https://pm-prediction.streamlit.app/
## Table of Contents
1. [Problem Statement](#problem-statement)
2. [Dataset Description](#dataset-description)
3. [Installation](#installation)
4. [Exploratory Data Analysis](#exploratory-data-analysis)
5. [Data Preprocessing](#data-preprocessing)
6. [Models trained](#models-trained)
7. [Results](#results)
8. [Model Deployment](#model-deployment)
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
### Note. You can download the dataset `pm_prediction_dataset.csv` provided above.

## Installation
To run the code in this repository, you need to have Python (version 3.9.13 recommended) installed. You can install the required packages using:

```bashfrequency 
pip install -r requirements.txt
```
## Exploratory Data Analysis
For detailed EDA, ydata_profiling library has been used. ydata-profiling is a valuable tool for data scientists and analysts because it streamlines EDA, provides comprehensive insights, enhances data quality, and promotes data science best practices.
### Note: You can refer `profile.html` provided above.

## Data Preprocessing
1. Since the dataset contains separate values of YEAR, MO, DY and HR, we need to first create a new column 'Date' which contain the values of columns 'YEAR', 'MO', 'DY', 'HR' and convert it into datetime format.
2. Set 'Date' column as index for the dataset.
3. Remove 'YEAR', 'MO', 'DY', 'HR' columns from the dataset to avoid redundancy.
4. Remove the null values from the dataset.
5. As our dataset contains hourly information of particulate matter data, we need to set frequency of our dataset as 'H'.
### Note: Detailed code has been provided in `PM_Prediction.ipynb`

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
#### Results Table PM2.5
![1 1](https://github.com/Tejas320/Particulate_Matter_Prediction/assets/73283098/a2102f4b-e5a5-4f6d-917d-7edfc8a2b022)
#### Results Table PM10
![1 2](https://github.com/Tejas320/Particulate_Matter_Prediction/assets/73283098/1a30d4c1-cc7a-43e3-b727-409e0a6545ac)
#### Model having low MAE, MSE, RMSE values and high R2 value is considered the best model, i.e. LSTM
### LSTM prediction on test data
![1 3](https://github.com/Tejas320/Particulate_Matter_Prediction/assets/73283098/d0999be0-2a0e-404d-b8df-7aec585c806e)
![1 4](https://github.com/Tejas320/Particulate_Matter_Prediction/assets/73283098/7629c9a6-de41-4405-94b0-32dadc04f8a9)
## Model Deployment
To make our particulate matter (PM) prediction model accessible and user-friendly, we deployed our best-performing LSTM model on Streamlit Cloud. This deployment enables users to interact with the model in real-time, and gain insights through an intuitive web interface. Streamlit Cloud simplifies the process of sharing our advanced predictive capabilities with a broader audience, facilitating informed decision-making for air quality management.

![Screenshot (87)](https://github.com/Tejas320/Particulate_Matter_Prediction/assets/73283098/97da2ecd-6dac-40b2-ab41-9e7cec352dcf)
![Screenshot (88)](https://github.com/Tejas320/Particulate_Matter_Prediction/assets/73283098/1ea38fd1-d2aa-4d76-9931-434d29f19ece)





