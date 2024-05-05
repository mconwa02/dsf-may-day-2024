# Data Science Festival May Day 2024

MLOPS in Financial Services

https://pypi.org/project/statsmodels/

https://pypi.org/project/scikit-learn/

https://pypi.org/project/sktime/

https://pypi.org/project/darts/

## Setting up the Development Environment

To ensure a clean and isolated development environment, use a 
virtual environment created with `venv` and manage dependencies using 
`pyproject.toml`. 

Additionally, set up pre-commit hooks for code quality checks, 
including linting with Ruff.

### Creating a Virtual Environment

Create and activate a virtual environment:
```bash
python -m venv venv
venv\Scripts\activate
```

### Installing Dependencies

Once inside the virtual environment, install project dependencies from the `pyproject.toml` file:
```bash
pip install -r pyproject.toml
```

### Setting up Pre-commit Hooks and Linting

Use `pre-commit` to enforce code quality standards. 
Additionally, use `ruff` for linting. 
Both packages are in the `pyproject.toml` file for install.

Navigate to your project directory and set up pre-commit hooks:
```bash
pre-commit install
```

A `.pre-commit-config.yaml` file is in project directory with config for 
ruff linting. Whenever you make a commit, `pre-commit` will run linting 
with Ruff and enforce code quality standards automatically.

### Statsmodels Example

An example of how you can use the statsmodels library in Python to 
build an ARIMA (AutoRegressive Integrated Moving Average) model for 
time series forecasting:
 
Make sure to replace 'your_data.csv' with the path to your actual data file. 
Adjust the values of p, d, and q according to your data and model requirements.
Also, consider whether differencing is necessary to make your data stationary,
and modify the code accordingly.

## Sktime Example

To build an ARIMA (AutoRegressive Integrated Moving Average) model using the 
sktime library in Python, you can use the `ARIMA` estimator provided by sktime.
In this example:

1. We load the Airline dataset, which is a univariate time series dataset included in sktime.
2. We split the dataset into training and testing sets.
3. We fit an ARIMA model to the training data using `ARIMA` estimator. You can specify the order of the ARIMA model using the `order` parameter.
4. We use the fitted model to make predictions for the testing set.
5. Finally, we plot the original data, the testing set, and the forecasted values.

This example demonstrates how to use sktime to build and evaluate an ARIMA 
model for time series forecasting. You can adjust the order of the ARIMA model
and other parameters according to your specific dataset and requirements.

### Darts (Data Analytics and Regression Testing Suite) Example

Darts is a library specifically designed for time series forecasting and 
analysis. It provides a convenient interface for building various 
forecasting models, including ARIMA (AutoRegressive Integrated Moving Average). 

You can adjust the hyperparameters of the ARIMA model and other settings 
according to your specific dataset and requirements.