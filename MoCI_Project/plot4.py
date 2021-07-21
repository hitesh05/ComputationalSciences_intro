import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import math

df = pd.read_csv('datasets/CSR.csv')

df =pd.melt(df, id_vars='Year', var_name='birth order', value_name='birth rate')

# print(df)

ax=sns.catplot(x='Year', y='birth rate', hue='birth order', data=df, kind='bar')
# ax.set_xticklabels(rotation=25, ha="right")
# plt.tight_layout()
plt.title("Child sex ratio by birth order")
plt.ylabel("Child sex ratio", fontsize=14)
plt.xlabel("Year", fontsize=12)
plt.ylim(850)
plt.savefig('datasets/CSR.png')
plt.show()