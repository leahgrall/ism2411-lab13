

#reflection 1: A boolean filter allows you to select specific rows from a DataFrame based on conditions. For example, you can filter sales data to only show rows from the South region.
#reflection 2: df["revenue"] selects one column as a Series, while df[["revenue"]] selects it as a DataFrame. This matters when you need to perform operations that require a DataFrame instead of a Series.
#reflection 3: The biggest reason to use pandas is that it makes organizing, filtering, and analyzing large amounts of data much faster and easier than doing everything manually in Excel.

print("--- exercise 1 ---")

import pandas as pd  # type: ignore[reportMissingModuleSource]

df = pd.read_csv("data/retail_sales.csv")

print(df.head())
print(df.shape)
print(df.columns.tolist())
print(df.dtypes)

print("--- exercise 2 ---")

south = df[df['region'] == 'South']

print(len(south))
print(south.head())

print("--- exercise 3 ---")

top_5 = df.sort_values('revenue', ascending=False).head(5)
print(top_5)

print("--- exercise 4 ---")

big_south = df[(df['region'] == 'South') & (df['revenue'] > 100000)]

print(len(big_south))
print(big_south.head())

print("--- exercise 5 ---")

df['per_unit'] = df['revenue'] / df['quantity']

print(df.head())
print(df['per_unit'].mean())

print("--- exercise 6 ---")

print(df['region'].unique())
print(df['region'].value_counts())

print("--- exercise 7 ---")

selected = df[['region', 'product', 'revenue']]

print(selected.shape)
print(selected.head())

print("--- exercise 8 ---")

df.to_csv('data/explored.csv', index=False)

print("File saved successfully!")

