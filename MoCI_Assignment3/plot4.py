import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

x = []
y = []

df = pd.read_csv('HS_datasets/Cashew.csv')
# print(df)

for ind in df.index:
    a = str(df['Year'][ind])
    b = df['Value'][ind]
    #print(a,b)
    x.append(a)
    y.append(b)
      
plt.title("Cashew exports")
plt.xlabel('Year')
plt.ylabel('Total Value')
#plt.yticks(y)
plt.plot(x, y)
  
plt.savefig('HS_datasets/cashew.png')