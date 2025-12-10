# -*- coding: utf-8 -*-
"""
Created on Mon Dec  1 21:06:09 2025

@author: Liang Gao
"""

#download the model with pkl as local lication
import joblib   
import numpy as np  
import pandas as pd 
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
############################################################################################################
## The introduction of model input parameters 
# real:      The real part of soil dielectric constant
# imaginary: The imaginary part of soil dielectric constant
# Moisture:  Soil moisture content
# Frequency: Microwave frequency (5 - 6 GHz)
# Sandy:     Soil sand fraction(0 - 1)
# Clay:      Soil clay fraction(0 - 1)
# rou_s:     Soil specific dendity 
# rou_b:     Soil bulk dendity 
#
##The introduction of model output parameters 
# Salinity: the predicted Soil salinity content (0 - 10 g/kg)

############################################################################################################
# Multi-Sample Batch Prediction for Soil Properties
##Load the saved model  
# this is an example about soil salinity content prediction model
# model_input_path is the address of the data storage folder
model_input_path = r'...\SscRetrieval_Cband010_RealImaginarySM.plk'
model_RF = joblib.load(model_input_path)

#Load the example dataset
# input_path_file is the address of the data storage folder
input_path_file = r'...\DCdataset_sample.csv'
data = pd.read_csv(input_path_file)
keys = data.keys()
data = data[data['frequency'] > 5]
data = data[data['frequency'] < 6]
data = data.dropna()
# choose the model parameters
X = data[['real','imaginary', 'moisture','frequency','Sandy', 'Clay', 'rou_s', 'rou_b']]
# choose the model prediction parameters
yy = data['salinity']  
#split example dataset as the train-samples and test-samples
# X_train, X_test, y_train, y_test = train_test_split(X, yy, test_size=0.7, random_state=42)
X_test = X
y_test = yy
# predict the real part of soil dielectric constant 
y_predict = model_RF.predict(X_test)
#
plt.figure(figsize=(7, 5), dpi=300)
plt.scatter(y_test, y_predict)
plt.xlabel('The True Value')
plt.ylabel('The Predicted Value')
plt.show()
############################################################################################################
#Single-Soil-Sample Prediction
##built the input variables X_test

X = {'real':[16.9],'imaginary':[9.9],'moisture':[0.2], 'frequency':[5.5],'Sandy': [0.46], 'Clay':[0.097], 'rou_s':[2.65], 'rou_b':[1.35]}
if (X['frequency'][0] < 5) or ((X['frequency'][0] > 6)):
    print('This model is not applicable within this frequency range.')
if ((X['moisture'][0] > 0.5)):
    print('This model is not applicable within this moisture range.')
X = pd.DataFrame(X)
y_predict = model_RF.predict(X)

#the soil properties input parameter X_text = [moisture, salinity, frequency, Sandy, Clay, rou_s, rou_b]

#moisture: soil moisture content, salinity: soil salinity content, frequency: microwave frequency,
#Sandy: soil sandy fraction, Clay: soil clay fraction, rou_s: soil specific density, rou_b: soil bulk density
#the unit of these input parameters are: moisture(m³/m³), salinity(g/kg), frequency(GHz), Sandy(%), Clay(%), rou_s(g/m³), rou_b(g/cm³),
