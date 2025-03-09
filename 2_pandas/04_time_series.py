import pandas as pd
import numpy as np

# Create a time series dataset
# print("Creating time series data:")
# dates = pd.date_range(start='2023-01-01', end='2023-03-01', freq='D')
# ts = pd.Series(np.random.randn(len(dates)).cumsum(), index=dates)
# print(ts.head())

#Resampling - aggregating to monthly frequency
# print("\n1. Monthly resampling (mean):")
# monthly = ts.resample('ME').mean()
# print(monthly)

# # Date shifting
# print("\n2. Shifting data forward by 2 days:")
# shifted = ts.shift(2)
# print(pd.concat([ts.head(), shifted.head()], axis=1, 
#                 keys=['Original', 'Shifted']))

# # Rolling window calculations
# print("\n3. 7-day rolling average:")
# rolling = ts.rolling(window=7).mean()
# print(pd.concat([ts.head(10), rolling.head(10)], axis=1, 
#                 keys=['Original', '7-Day Avg']))

# # # Seasonal decomposition
# print("\n4. Creating seasonal data and decomposing it:")
# # Creating more obvious seasonal data
# seasonal_range = pd.date_range('2020-01-01', '2022-12-31', freq='D')
# seasonal_data = pd.Series(
#     np.sin(np.arange(len(seasonal_range)) * 2 * np.pi / 365.25) * 10 + 
#     np.random.randn(len(seasonal_range)) * 3 +
#     np.arange(len(seasonal_range)) * 0.05,  # Adding trend
#     index=seasonal_range
# )

# try:
#     from statsmodels.tsa.seasonal import seasonal_decompose
#     decomposition = seasonal_decompose(seasonal_data, model='additive', period=365)
#     print("Decomposition components available:", decomposition.seasonal.head())
# except ImportError:
#     print("statsmodels not installed. Install with: pip install statsmodels")

# # Time-based indexing
# print("\n5. Selecting data by time period:")
# print("Data for February 2023:")
# print(ts['2023-02'])

# print("\nData between specific dates:")
# print(ts['2023-01-15':'2023-01-20'])

# # Time zone handling
# print("\n6. Time zone conversion:")
# ts_utc = pd.Series(np.random.randn(3), 
#                   index=pd.date_range('2023-01-01', periods=3, freq='D', tz='UTC'))
# print("UTC time series:")
# print(ts_utc)

# print("\nConverted to US Eastern time:")
# ts_est = ts_utc.tz_convert('US/Eastern')
# print(ts_est)

# # Creating a DataFrame with multiple time series
# print("\n7. Multiple time series in a DataFrame:")
# df_ts = pd.DataFrame({
#     'A': np.random.randn(len(dates)).cumsum(),
#     'B': np.random.randn(len(dates)).cumsum(),
#     'C': np.random.randn(len(dates)).cumsum()
# }, index=dates)
# print(df_ts.head())

# # Time period calculations
# print("\n8. Year-to-date calculation:")
# year_start = pd.Timestamp('2023-01-01')
# ytd_data = df_ts[df_ts.index >= year_start]
# print(f"YTD change in A: {ytd_data['A'][-1] - ytd_data['A'][0]:.2f}")
