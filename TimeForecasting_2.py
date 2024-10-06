import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA
from statsmodels.tsa.stattools import adfuller
from sklearn.metrics import mean_squared_error

def test_stationarity(timeseries):
    result = adfuller(timeseries)
    print('ADF Statistic:', result[0])
    print('p-value:', result[1])
    return result[1]


file_path = 'C:\\Users\\susmi\\OneDrive\\Desktop\\IITK\\archive\\city_day.csv'

data = pd.read_csv(file_path, usecols=[1, 2], names=['date', 'PM2.5'], header=0)

data['date'] = pd.to_datetime(data['date'])
data.set_index('date', inplace=True)
# p_value = test_stationarity(data['PM2.5'])
# if p_value > 0.05:
#     # Apply differencing to make data stationary
#     data['PM2.5'] = data['PM2.5'].diff().dropna()

data.dropna(inplace=True)

# Split the data into training and testing sets
train_size = int(len(data) * 0.8)
train, test = data[:train_size], data[train_size:]

# 2. Model Training
model = ARIMA(train['PM2.5'], order=(5, 1, 0))
model_fit = model.fit()

# 3. Prediction
predictions = model_fit.forecast(steps=len(test))
predictions_index = test.index
predictions_df = pd.DataFrame(data=predictions, index=predictions_index, columns=['Predicted PM2.5'])

# 4. Visualization with Different Colors
plt.figure(figsize=(14, 7))

# Training data in blue
plt.plot(train.index, train['PM2.5'], color='blue', label='Training Data', alpha=0.5)

# Actual test data in green
plt.plot(test.index, test['PM2.5'], color='green', label='Actual PM2.5', alpha=0.5)

# Predicted data in red
plt.plot(predictions_df.index, predictions_df['Predicted PM2.5'], color='red', label='Predicted PM2.5', alpha=0.7)

# Highlight the area of predictions
plt.fill_between(predictions_df.index, predictions_df['Predicted PM2.5'], color='red', alpha=0.1)

plt.title('PM2.5 Prediction')
plt.xlabel('Date')
plt.ylabel('PM2.5 Levels')
plt.legend()
plt.show()

# Print Mean Squared Error
mse = mean_squared_error(test['PM2.5'], predictions)
print(f'Mean Squared Error: {mse}')

