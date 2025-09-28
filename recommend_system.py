import pandas as pd
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori, association_rules


# !pip install mlxtend
# Load dataset
df = pd.read_csv('../data/transactions.csv')  # Adjust path if needed
print("Dataset loaded successfully!")
print(df.head())

# Step 4.4: Prepare transactions
transactions = df.groupby('TransactionID')['Product'].apply(list).tolist()

# Step 4.5: Encode transactions
te = TransactionEncoder()
te_ary = te.fit(transactions).transform(transactions)
df_encoded = pd.DataFrame(te_ary, columns=te.columns_)

# Step 4.6: Find frequent itemsets
frequent_itemsets = apriori(df_encoded, min_support=0.01, use_colnames=True)
print("Frequent itemsets:")
print(frequent_itemsets.head())

# Step 4.7: Generate association rules
rules = association_rules(frequent_itemsets, metric="lift", min_threshold=1.0)
print("Top association rules:")
print(rules.head())
