
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from darts import TimeSeries
from darts.models import ARIMA

# Load your time series data into a pandas DataFrame
# For example:
# data = pd.read_csv('your_data.csv')

# Assuming your data has a 'date' column, set it as the index
# data['date'] = pd.to_datetime(data['date'])
# data.set_index('date', inplace=True)

# Convert your pandas DataFrame into a Darts TimeSeries object
series = TimeSeries.from_dataframe(data, 'date', 'value')

# Split the series into training and testing sets
train_size = int(0.8 * len(series))
train, test = series[:train_size], series[train_size:]

# Fit an ARIMA model
model = ARIMA()
model.fit(train)

# Forecast future values
forecast = model.predict(len(test))

# Plot the original data and the forecast
series.plot(label='Original Data')
forecast.plot(label='Forecast', lw=2)
plt.xlabel('Date')
plt.ylabel('Value')
plt.title('ARIMA Forecast')
plt.legend()
plt.show()

