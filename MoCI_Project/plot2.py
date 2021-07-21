import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import math

df = pd.read_csv('/home/hitesh/Documents/IIIT-H/HS/History/Project/datasets/Infant-Mortality.csv')
df_1 = pd.DataFrame()
df_2 = pd.DataFrame()

df_1['States'] = df['States']
df_1['Males'] = df['Male_1961']
df_1['Females'] = df['Female_1961']
# df_1['Total'] = df['Total_1961']

df_1 = pd.melt(df_1, id_vars='States', var_name='Gender', value_name='mortality rate_1961')

df_2['States'] = df['States']
df_2['Males'] = df['Male_1981']
df_2['Females'] = df['Female_1981']
# df_2['Total'] = df['Total_1981']

df_2 = pd.melt(df_2, id_vars='States', var_name='Gender', value_name='mortality rate_1981')

ax1=sns.catplot(x='States', y='mortality rate_1961', hue='Gender', data=df_1, kind='bar')
ax1.set_xticklabels(rotation=25, ha="right")

# ax1=sns.catplot(x='States', y='mortality rate_1981', hue='Gender', data=df_2, kind='bar')
# ax1.set_xticklabels(rotation=25, ha='right')
# plt.tight_layout()
plt.title("Mortality Rates in 1961")
plt.ylabel("Mortality (per 1000)", fontsize=12)
plt.xlabel("States", fontsize=12)
#plt.savefig('datasets/Infant_Mortality_1981.png')
plt.show()