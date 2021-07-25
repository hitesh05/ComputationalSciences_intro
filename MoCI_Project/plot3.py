import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('datasets/sex-ratio.csv')
# df = pd.read_csv('datasets/CSR-3.csv')

# year = df['Year']
# ratio = df['Ratio']

year = df['Year']
ratio = df['Ratio']

plt.plot(year,ratio,color='b')

plt.title('Sex Ratio over the years')
# plt.title('Child Sex Ratio over the years')
plt.xlabel('Year')
plt.ylabel('Sex ratio')
plt.savefig('datasets/sex-ratio.png')
# plt.savefig('datasets/CSR-3.png')
plt.show()
