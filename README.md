# Machine-Learning-soil-dielectric-constant
A Universal and Practical Soil Dielectric Constant Model constructed based on machine learning could used to simulate soil mixture medium dielectric properties and retrieve soil water content and salinity content

## introduction
The build soil dielectric constant model can be used in an border application conditions. Specifically, the operating frequency range is 0.2–20 GHz, the soil moisture content range is 0.05–0.4 m³/m³, and the soil salinity content range is 0–100 g/kg,<br>

These soil dielectric constant models were built based on Random Forest algorithm through theoptimal model value, which was proven has the high-accuracy to simulating the soil dielectric properties,<br>

##The model materials introduction<br>
Datasets:           The Datasets folder contains a sample dataset that can be used to verify whether the model works properly.<br>
EXample:            The Example folder contains sample data and example Python scripts for the soil dielectric constant real-part model.<br>
Forward_models:     The Forward_models folder includes predictive models for the real and imaginary parts of the soil dielectric constant, along with corresponding example Python scripts for their use.<br>
SM_Retrieval_Model: The SM Retrieval_Model folder contains soil moisture content predictive models for various scenarios, along with corresponding example Python scripts for their use.
Ssc_Retrieval_Model: The SscRetrieval_Model folder contains soil moisture content predictive models for various scenarios, along with corresponding example Python scripts for their use.

##The underlying foundational environment<br>
windows 10<br>
python==3.11<br>


##The required base packages and recommended versions<br>
joblib      1.2.0<br>
numpy       1.26.4<br>
pandas      2.1.4<br>
sklearn     1.2.2<br>
matplotlib  3.8.0<br>

## The example to using soil dielectric constant predicted models

the soil dielectric constant model can be devide as the real part of soil dielectric constant model and imaginary part of the soil dielectric constant prediced model
the developed soil dielectric constant models were saved in the Folder "Forward_models"

the pathway to predict real or imaginary of soil dielectric constant using the developed soil dielectric constant model

```
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
# real: the predicted real part of soil dielectric constant

############################################################################################################
# Multi-Sample Batch Prediction for Soil Properties
##Load the saved soil dielectric constant model  
# this is an example about soil dielectric constant real part prediction model
# model_input_path is the address of the data storage folder
model_input_path = r'...\Real_model.plk'
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
yy = data['real']  
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
X = {'moisture':[0.2], 'salinity':[2],'frequency':[5.5],'Sandy': [0.46], 'Clay':[0.097], 'rou_s':[2.65], 'rou_b':[1.35]}
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

```

## The example to using developed soil moisture and salinity retrieval models

##the retrieval model can be used to retrieve soil moisture and salinity based on the real imaginary part of 
the soil dielectric constant prediced model and other soil properties

the developed soil dielectric constant models were saved in the Folder "SM_retrieval_model"

the pathway to retrieve soil moisture or salinity using the developed retrieval model

```
#download the model with pkl as local lication
import joblib      

##Load the saved soil dielectric constant model  
model_RF = joblib.load('SMRetrieval_ReallmaginarySsm.pkl')

##built the input variables X_test

#the retrieval model including numerous pattern of retrieve soil moisture or salinity based on soil dielectric properties,
the different model has different input parameters

#A detailed description of these parameters is provided in the readme.txt file within the SM_retrieval_model folder.

#This table shows the input parameters for the widely-used retrieval model 'SMRetrieval_ReallmaginarySsm.pkl'.

X_text = [,,,,]
#the soil properties input parameter X_text = [real, imaginary, frequency, salinity, Sandy,  Clay, rou_s, rou_b]

#real: real part of soil dielectric constant,imaginary: imaginary part of soil dielectric constant,
#salinity: soil salinity content, frequency: microwave frequency,
#Sandy: soil sandy fraction, Clay: soil clay fraction, rou_s: soil specific density, rou_b: soil bulk density

#the unit of these input parameters are: moisture(m³/m³), salinity(kg/kg), frequency(GHz), Sandy(%), Clay(%), rou_s(kg/m³), rou_b(kg/m³), 
SM_predict = model_RF.predict(X_test)
```
##Reference,<br>
M. C. Dobson, F. T. Ulaby, M. T. Hallikainen et al., “Microwave dielectric behavior of wet soil-Part2: Dielectric mixing models,” IEEE Transactions on Geoscience and Remote Sensing, vol. 23, no. 1, pp. 35-46, 1985.,<br>
Y. Wu, W. Wang, S. Zhao et al., “Dielectric properties of saline soils and an improved dielectric model in C-band,” IEEE Transactions on Geoscience and Remote Sensing, vol. 53, no. 1, pp. 440-452, 2014.,<br>
G. C. Topp, J. L. Davis, and A. P. Annan, “Electromagnetic determination of soil water content: Measurements in coaxial transmission lines,” Water resources research, vol. 16, no. 3, pp. 574-582, 1980.
