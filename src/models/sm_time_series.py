import matplotlib.pyplot as plt
import pandas as pd
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
from statsmodels.tsa.arima.model import ARIMA

data = pd.read_csv(r"C:\dev\data\dsf\product_info_simple_final_train.csv")

# Assuming your data has a 'date' column, set it as the index
data["transaction_date"] = pd.to_datetime(data["transaction_date"], format="%Y%m%d")
data = data.set_index("transaction_date")

# Check if your data is stationary or not
# If not, you may need to difference it to make it stationary
stationary_data = data["apply_amt"].diff().dropna()

# Plot the ACF and PACF to determine the order of AR and MA terms
plot_acf(stationary_data)
plot_pacf(stationary_data)
# plt.show()

# Define the order of the ARIMA model (p, d, q)
# p: number of autoregressive terms
# d: number of differences
# q: number of moving average terms
p = 1  # Example value
d = 1  # Example value
q = 1  # Example value

# Fit the ARIMA model
model = ARIMA(stationary_data, order=(p, d, q))
results = model.fit()

# Forecast future values
forecast_steps = 10  # Example value
forecast = results.forecast(steps=forecast_steps)

# Plot the original data and the forecast
plt.plot(stationary_data.index, stationary_data.values, label="Original Data")
plt.plot(
    pd.date_range(
        start=stationary_data.index[-1], periods=forecast_steps + 1, freq="D"
    )[1:],
    forecast,
    label="Forecast",
)
plt.xlabel("Date")
plt.ylabel("Value")
plt.title("ARIMA Forecast")
plt.legend()
# plt.show()
