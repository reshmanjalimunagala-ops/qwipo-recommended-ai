import pandas as pd
# Load dataset
df = pd.read_csv('../data/transactions.csv')  # path from src folder to data folder
# Display first 5 rows
print("Dataset loaded successfully!")
print(df.head())
