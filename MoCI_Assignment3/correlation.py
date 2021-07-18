import pandas as pd
import matplotlib.pyplot as plt
from tabulate import tabulate

df1 = pd.read_csv('HS_datasets/per-capita.csv')
df2 = pd.read_csv('HS_datasets/ExportsVsImports.csv')
# print(df1)
# print(df2)

#merge 2 dataframes:
# merged_df = pd.merge(df1,df2,on='States/UTs',left_on='Urban Male', right_on='Urban GFR', how='inner')
merged_df = pd.merge(df1,df2, on='Year', how='inner')
#print(merged_df)
print(tabulate(merged_df, tablefmt = 'psql'))

print("per capita income and exports: ")
column_1 = merged_df["Income"]
column_2 = merged_df["Exports"]
correlation = column_1.corr(column_2)
print(correlation)
print()