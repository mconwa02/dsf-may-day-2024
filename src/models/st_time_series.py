from sktime.datasets import load_airline
from sktime.forecasting.arima import ARIMA, AutoARIMA
from sktime.utils.plotting import plot_series

# Load the Airline dataset (a univariate time series dataset)
y = load_airline()

# Split the data into training and testing sets
train_size = int(0.8 * len(y))
train, test = y[:train_size], y[train_size:]

# Fit an ARIMA model
# Specify the order of the ARIMA model (p, d, q)
# p: number of autoregressive terms
# d: number of differences
# q: number of moving average terms
model = ARIMA(order=(1, 1, 1))
model.fit(train)

# Forecast future values
forecast_horizon = len(test)
y_pred = model.predict(fh=forecast_horizon)

# Plot the original data and the forecast
plot_series(train, test, y_pred, labels=["Train", "Test", "Forecast"])
plt.title('ARIMA Forecast')
plt.show()
