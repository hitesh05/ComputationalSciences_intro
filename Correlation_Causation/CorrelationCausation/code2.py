import pandas as pd

df1 = pd.read_csv('datasets/literacy-rate.csv')
df2 = pd.read_csv('datasets/infant_mortality.csv')
# print(df1)
# print(df2)

#merge 2 dataframes:]
merged_df = pd.merge(df1,df2, on='States/UTs', how='inner')
#print(merged_df)

column_1 = merged_df["Persons"]
column_2 = merged_df["Total"]
correlation = column_1.corr(column_2)
print("Total literacy and total mortality: ",correlation)
#print(correlation)
print()

column_1 = merged_df["Persons"]
column_2 = merged_df["Total Female"]
correlation = column_1.corr(column_2)
print("Total literacy and female mortality: ",correlation)
#print(correlation)
print()

column_1 = merged_df["Rural Persons"]
column_2 = merged_df["Rural Totals"]
correlation = column_1.corr(column_2)
print("Rural literacy and rural mortality: ",correlation)
#print(correlation)
print()

column_1 = merged_df["Rural Persons"]
column_2 = merged_df["Rural Females"]
correlation = column_1.corr(column_2)
print("Rural literacy and rural female mortality: ",correlation)
#print(correlation)
print()

column_1 = merged_df["Urban Persons"]
column_2 = merged_df["Urban Totals"]
correlation = column_1.corr(column_2)
print("Urban literacy and urban mortality: ",correlation)
#print(correlation)
print()

column_1 = merged_df["Urban Persons"]
column_2 = merged_df["Urban Females"]
correlation = column_1.corr(column_2)
print("Urban literacy and urban female mortality: ",correlation)
#print(correlation)
print()

column_1 = merged_df["Rural Male"]
column_2 = merged_df["Rural Totals"]
correlation = column_1.corr(column_2)
print("Rural male litearcy and rural mortality: ",correlation)
#print(correlation)
print()

column_1 = merged_df["Urban Male"]
column_2 = merged_df["Urban Totals"]
correlation = column_1.corr(column_2)
print("Urban male literacy and urban mortality: ",correlation)
#print(correlation)
print()

column_1 = merged_df["Rural Female"]
column_2 = merged_df["Rural Totals"]
correlation = column_1.corr(column_2)
print("Rural female literacy and rural mortality: ",correlation)
#print(correlation)
print()

column_1 = merged_df["Urban Female"]
column_2 = merged_df["Urban Totals"]
correlation = column_1.corr(column_2)
print("Urban female literacy and urban mortality: ",correlation)
#print(correlation)
print()