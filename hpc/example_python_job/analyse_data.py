#!/usr/bin/env python3
import pandas as pd

# Read the CSV file directly
print("Reading my_data.csv...")
data = pd.read_csv('my_data.csv')

# Display basic information
print(f"\nFound {len(data)} rows and {len(data.columns)} columns")
print(f"Column names: {', '.join(data.columns)}")
