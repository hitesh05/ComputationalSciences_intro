import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

year = []
primary = []
secondary = []
tertiary = []

df = pd.read_csv('HS_datasets/industry-contribution.csv')

for ind in df.index:
    a = str(df['Year'][ind])
    b = df['Primary'][ind]
    c = df['Secondary'][ind]
    d = df['Tertiary'][ind]

    year.append(a)
    primary.append(b)
    secondary.append(c)
    tertiary.append(d)
    #print(a,b,c,d)

plt.title('Contribution of different sectors to GDP')
plt.xlabel('Year')
plt.ylabel('Percentage contribution')

plt.plot(year,primary,color='g', label='primary')
plt.plot(year,secondary,color='r', label='secondary')
plt.plot(year,tertiary,color='b', label='tertiary')

plt.legend()
plt.savefig('HS_datasets/industry-contribution.png')