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
# Moisture:  Soil moisture content (0 - 0.4 m³/m³)
# Salinity:  Soil salinity content (0 - 100 g/kg)
# Frequency: Microwave frequency (0.2 - 20 GHz)
# Sandy:     Soil sand fraction(0 - 1)
# Clay:      Soil clay fraction(0 - 1)
# rou_s:     Soil specific dendity 
# rou_b:     Soil bulk dendity 
#
##The introduction of model output parameters 
# imaginary: the predicted imaginary part of soil dielectric constant

############################################################################################################
# Multi-Sample Batch Prediction for Soil Properties
##Load the saved soil dielectric constant model  
# This is an example of a predictive model for the imaginary part of the dielectric constant.
# model_input_path is the address of the data storage folder
model_input_path = r'...\Imaginary_model.plk'
model_RF = joblib.load(model_input_path)

#Load the example dataset
# input_path_file is the address of the data storage folder
input_path_file = r'...\DCdataset_sample.csv'
data = pd.read_csv(input_path_file)
keys = data.keys()
data = data.dropna()
# choose the model parameters
X = data[['moisture', 'salinity', 'frequency','Sandy', 'Clay', 'rou_s', 'rou_b']]
# choose the model prediction parameters
yy = data['imaginary']  
#split example dataset as the train-samples and test-samples
X_train, X_test, y_train, y_test = train_test_split(X, yy, test_size=0.7, random_state=42)
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
X = {'moisture':[0.2],'salinity':[0.02], 'frequency':[5.5],'Sandy': [0.46], 'Clay':[0.097], 'rou_s':[2.65], 'rou_b':[1.35]}
if (X['frequency'][0] < 0.2) or ((X['frequency'][0] > 20)):
    print('This model is not applicable within this frequency range.')
if ((X['salinity'][0] > 100)):
    print('This model is not applicable within this salinity range.')
if ((X['moisture'][0] > 0.4)):
    print('This model is not applicable within this moisture range.')
X = pd.DataFrame(X)
y_predict = model_RF.predict(X)


#moisture: soil moisture content, salinity: soil salinity content, frequency: microwave frequency,
#Sandy: soil sandy fraction, Clay: soil clay fraction, rou_s: soil specific density, rou_b: soil bulk density

#the unit of these input parameters are: moisture(m³/m³), salinity(g/kg), frequency(GHz), Sandy(%), Clay(%), rou_s(g/m³), rou_b(g/cm³),


