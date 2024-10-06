import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA
from sklearn.metrics import mean_squared_error

np.random.seed(42)
date_rng = pd.date_range(start='2020-01-01', end='2023-12-31', freq='D')
pm25_values = np.random.randint(20, 150, size=(len(date_rng)))

data = pd.DataFrame(date_rng, columns=['date'])
data['PM2.5'] = pm25_values
data.set_index('date', inplace=True)

train_size = int(len(data) * 0.8)
train, test = data[:train_size], data[train_size:]

model = ARIMA(train['PM2.5'], order=(5, 1, 0))  # Example order
model_fit = model.fit()

predictions = model_fit.forecast(steps=len(test))
predictions_index = test.index

predictions_df = pd.DataFrame(data=predictions, index=predictions_index, columns=['Predicted PM2.5'])



plt.figure(figsize=(14, 7))

plt.plot(train.index, train['PM2.5'], color='blue', label='Training Data', alpha=0.5)

plt.plot(test.index, test['PM2.5'], color='green', label='Actual PM2.5', alpha=0.5)

plt.plot(predictions_df.index, predictions_df['Predicted PM2.5'], color='red', label='Predicted PM2.5', alpha=0.7)

plt.title('PM2.5 Prediction')
plt.xlabel('Date')
plt.ylabel('PM2.5 Levels')
plt.legend()
plt.show()


mse = mean_squared_error(test['PM2.5'], predictions)
print(f'Mean Squared Error: {mse}')
