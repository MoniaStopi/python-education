# Load pandas
import pandas as pd
import matplotlib.pyplot as plo
# Read in dataset
trends = pd.read_csv("datasets/trends_kj_sisters.csv")
# Make column names easier to work with
trends.columns = ["month", "kim", "khloe", "kourtney", "kendall", "kylie"]

for column in trends.columns:
    if "<" in trends[column].to_string():
        trends[column] = trends[column].str.replace("<", "")
        trends[column] = pd.to_numeric(trends[column])

trends.month = pd.to_datetime(trends.month)
trends.info()
trends.head()

# Set month as DataFrame index
trends = trends.set_index("month")

# Inspect the data
trends.head()
trends.plot()
trends.loc['2014-01-01':].plot()
# Smooth the data with rolling means
trends.rolling(12).mean().plot()

# Average search interest for each family line
trends["kardashian"] = (trends.kim + trends.khloe + trends.kourtney)/3
trends["jenner"] = (trends.kendall + trends.kylie)/2

# Plot average family line search interest vs. month
trends[['kardashian','jenner']].plot()