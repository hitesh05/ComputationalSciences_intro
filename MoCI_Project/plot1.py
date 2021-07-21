import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import math

df = pd.read_csv('datasets/sex-ratio-1990.csv')
df_2 = pd.DataFrame()
a=[]
b=[]
c=[]

for ind in df.index:
    x = math.floor((df['1'][ind] + df['2'][ind] + df['3'][ind])/3)
    y = math.floor((df['4'][ind] + df['5'][ind] + df['6'][ind])/3)

    a.append(x)
    b.append(y)
    c.append(df['States'][ind])

#print(a,b,c)

df_2['States'] = c
df_2['0-29'] = a
df_2['30+'] = b
# print(df_2)

df_2 = pd.melt(df_2, id_vars='States', var_name='age', value_name='sex ratio')
# print(df_2)

ax=sns.catplot(x='States', y='sex ratio', hue='age', data=df_2, kind='bar')
ax.set_xticklabels(rotation=25, ha="right")
# plt.tight_layout()
plt.title("Sex Ratio divided by age group")
plt.ylabel("Sex Ratio", fontsize=12)
plt.xlabel("States", fontsize=12)
plt.ylim(80)
# plt.savefig('datasets/sex-ratio.png')
plt.show()