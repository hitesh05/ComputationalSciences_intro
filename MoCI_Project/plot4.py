import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import math

# df = pd.read_csv('datasets/CSR.csv')
df = pd.read_csv('datasets/CSR-2.csv')

df =pd.melt(df, id_vars='Area', var_name='birth order', value_name='sex ratio')

# print(df)

ax=sns.catplot(x='Area', y='sex ratio', hue='birth order', data=df, kind='bar')
ax.set_xticklabels(rotation=25, ha="right")

plt.title("Child sex ratio of 2nd birth")
plt.ylabel("sex ratio", fontsize=14)
plt.xlabel("Area", fontsize=12)
plt.ylim(400)
plt.savefig('datasets/CSR-2.png')
plt.show()