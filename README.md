# Machine-Learning-soil-dielectric-constant
A Universal and Practical Soil Dielectric Constant Model constructed based on machine learning could used to simulate soil mixture medium dielectric properties and retrieve soil water content and salinity content

## introduction
The build soil dielectric constant model can be used in an border application conditions. Specifically, the operating frequency range is 0.4–20 GHz, the soil moisture content range is 0.05–0.4 m³/m³, and the soil salinity content range is 0–100 g/kg.

These soil dielectric constant models were built based on Random Forest algorithm through theoptimal model value, which was proven has the high-accuracy to simulating the soil dielectric properties.

##The underlying foundational environment,<br>
windows 10,<br>
python==3.11,<br>
other python maybe could  

##The required base packages
joblib,

## The example to using built model
```
#download the model with pkl as local lication
import joblib      

##Load the saved soil dielectric constant model  
model_RF = joblib.load('example.pkl')

##built the input variables X_test
X_text = [,,,,]
#the soil properties input parameter X_text = [moisture, salinity, frequency, Sandy, Clay, rou_s, rou_b]
#the unit of these input parameters are: moisture(m³/m³), salinity(kg/kg), frequency(GHz), Sandy(%), Clay(%), rou_s(kg/m³), rou_b(kg/m³), 
y_predict = model_RF.predict(X_test)
```
## The example to using built model
```
#download the model with pkl as local lication
import joblib      

##Load the saved soil dielectric constant model  
model_RF = joblib.load('example.pkl')

##built the input variables X_test
X_text = [,,,,]
#the soil properties input parameter X_text = [moisture, salinity, frequency, Sandy, Clay, rou_s, rou_b]
#the unit of these input parameters are: moisture(m³/m³), salinity(kg/kg), frequency(GHz), Sandy(%), Clay(%), rou_s(kg/m³), rou_b(kg/m³), 
y_predict = model_RF.predict(X_test)
```
