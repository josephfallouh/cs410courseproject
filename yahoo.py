import yfinance as yf
import pandas as pd
import os

# Define the stock ticker and date range
ticker = "TSLA"
start_date = "2022-07-03"
end_date = "2022-07-16"

# File path
file_path = "TSLA_stock_data.csv"

# Remove existing file if it exists
if os.path.exists(file_path):
    os.remove(file_path)

# Download historical data
stock_data = yf.download(ticker, start=start_date, end=end_date, interval="1d")

# Reset index and clean up the data
stock_data.reset_index(inplace=True)
stock_data['Date'] = pd.to_datetime(stock_data['Date']).dt.date  # Convert to date (if needed)
stock_data = stock_data.round(2)  # Round to 2 decimal places

# Rearrange columns (if needed)
stock_data = stock_data[['Date', 'Adj Close', 'Close', 'High', 'Low', 'Open', 'Volume']]

# Save to CSV without adding an index column
stock_data.to_csv(file_path, index=False)

# Display the data
print(stock_data)
