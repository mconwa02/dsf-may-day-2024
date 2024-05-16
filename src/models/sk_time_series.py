import matplotlib.pyplot as plt
import pandas as pd
from sktime.forecasting.arima import ARIMA
from sktime.utils.plotting import plot_series

df = pd.read_csv(r"C:\dev\data\dsf\product_info_simple_final_train.csv")
df["transaction_date"] = pd.to_datetime(df["transaction_date"], format="%Y%m%d")
df = df.set_index("transaction_date")
df.index.freq = "D"

y = df["apply_amt"]

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
plt.title("ARIMA Forecast")
plt.show()
