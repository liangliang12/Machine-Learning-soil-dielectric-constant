# Machine-Learning-soil-dielectric-constant
A Universal and Practical Soil Dielectric Constant Model constructed based on machine learning could used to simulate soil mixture medium dielectric properties and retrieve soil water content and salinity content

## introduction
The build soil dielectric constant model can be used in an border application conditions. Specifically, the operating frequency range is 0.4–20 GHz, the soil moisture content range is 0.05–0.4 m³/m³, and the soil salinity content range is 0–100 g/kg,<br>

These soil dielectric constant models were built based on Random Forest algorithm through theoptimal model value, which was proven has the high-accuracy to simulating the soil dielectric properties,<br>

##The underlying foundational environment,<br>
windows 10,<br>
python==3.11,<br>
other python maybe could  

##The required base packages,<br>
joblib,

## The example to using soil dielectric constant predicted models

the soil dielectric constant model can be devide as the real part of soil dielectric constant model and imaginary part of the soil dielectric constant prediced model
the developed soil dielectric constant models were saved in the Folder "Forward_models"

the pathway to predict real or imaginary of soil dielectric constant using the developed soil dielectric constant model

```
#download the model with pkl as local lication
import joblib      

##Load the saved soil dielectric constant model  
model_RF = joblib.load('example.pkl')

##built the input variables X_test
X_text = [,,,,]
#the soil properties input parameter X_text = [moisture, salinity, frequency, Sandy, Clay, rou_s, rou_b]

#moisture: soil moisture content, salinity: soil salinity content, frequency: microwave frequency,
#Sandy: soil sandy fraction, Clay: soil clay fraction, rou_s: soil specific density, rou_b: soil bulk density

#the unit of these input parameters are: moisture(m³/m³), salinity(kg/kg), frequency(GHz), Sandy(%), Clay(%), rou_s(kg/m³), rou_b(kg/m³),

DC_real = model_RF.predict(X_test)
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
#Reference
M. C. Dobson, F. T. Ulaby, M. T. Hallikainen et al., “Microwave dielectric behavior of wet soil-Part2: Dielectric mixing models,” IEEE Transactions on Geoscience and Remote Sensing, vol. 23, no. 1, pp. 35-46, 1985.
Y. Wu, W. Wang, S. Zhao et al., “Dielectric properties of saline soils and an improved dielectric model in C-band,” IEEE Transactions on Geoscience and Remote Sensing, vol. 53, no. 1, pp. 440-452, 2014.
G. C. Topp, J. L. Davis, and A. P. Annan, “Electromagnetic determination of soil water content: Measurements in coaxial transmission lines,” Water resources research, vol. 16, no. 3, pp. 574-582, 1980.
