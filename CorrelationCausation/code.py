import pandas as pd

df1 = pd.read_csv('datasets/literacy-rate.csv')
df2 = pd.read_csv('datasets/fertility-rate.csv')
# print(df1)
# print(df2)

#merge 2 dataframes:
# merged_df = pd.merge(df1,df2,on='States/UTs',left_on='Urban Male', right_on='Urban GFR', how='inner')
merged_df = pd.merge(df1,df2, on='States/UTs', how='inner')
#print(merged_df)

print("Persons and Total GFR: ")
column_1 = merged_df["Persons"]
column_2 = merged_df["Total GFR"]
correlation = column_1.corr(column_2)
print(correlation)
print()

print("Urban Female and Urban GFR")
column_1 = merged_df["Urban Female"]
column_2 = merged_df["Urban GFR"]
correlation = column_1.corr(column_2)
print(correlation)
print()

print("Rural Female and Rural GFR")
column_1 = merged_df["Rural Female"]
column_2 = merged_df["Rural GFR"]
correlation = column_1.corr(column_2)
print(correlation)
print()

print("Urban Male and Urban GFR")
column_1 = merged_df["Urban Male"]
column_2 = merged_df["Urban GFR"]
correlation = column_1.corr(column_2)
print(correlation)
print()

print("Rural Male and Rural GFR")
column_1 = merged_df["Rural Male"]
column_2 = merged_df["Rural GFR"]
correlation = column_1.corr(column_2)
print(correlation)
print()

