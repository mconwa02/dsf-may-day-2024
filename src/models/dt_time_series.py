import matplotlib.pyplot as plt
import pandas as pd
from darts import TimeSeries
from darts.models import ARIMA

data = pd.read_csv(r"C:\dev\data\dsf\product_info_simple_final_train.csv")

# Assuming your data has a 'date' column, set it as the index
data["date"] = pd.to_datetime(data["transaction_date"])

# pick one product with a least 30 values
data = data[data["product_pid"] == "product100"]

# Convert your pandas DataFrame into a Darts TimeSeries object
series = TimeSeries.from_dataframe(
    data,
    time_col="transaction_date",
    value_cols="apply_amt",
    fill_missing_dates=True,
    freq=1,
)

# Split the series into training and testing sets
train_size = int(0.8 * len(series))
train, test = series[:train_size], series[train_size:]

# Fit an ARIMA model
model = ARIMA()
model.fit(train)

# Forecast future values
forecast = model.predict(len(test))

# Plot the original data and the forecast
series.plot(label="Original Data")
forecast.plot(label="Forecast", lw=2)
plt.xlabel("Date")
plt.ylabel("Total Amt")
plt.title("ARIMA Forecast")
plt.legend()
plt.show()
