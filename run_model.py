import joblib 
import pandas as pd

model = joblib.load('AQI_GradientBoosting.pkl')

future_X = pd.DataFrame({'PM2.5' : [25.58],'PM10' : [91.73],'NO': [17.5],'NO2': [39.32], 'NOx': [20.13], 'NH3': [5.7], 'CO': [0.02], 'SO2': [10.14], 'O3': [2.3], 'Benzene': [5.97], 'Toluene': [15.23], 'Xylene': [4.13]})

print(future_X)

future_PM2_5 = model.predict(future_X)
print(f'Predicted PM2.5 for the given values : {future_PM2_5[0]:.2f}')