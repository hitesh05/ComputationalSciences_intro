import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('datasets/sex-ratio.csv')

year = df['Year']
ratio = df['Ratio']

plt.plot(year,ratio,color='b')

plt.title('Sex Ratio over the years')
plt.xlabel('Year')
plt.ylabel('Sex ratio')
plt.savefig('datasets/sex-ratio.png')
plt.show()
