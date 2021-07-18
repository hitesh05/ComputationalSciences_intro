import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

x = []
y = []

df = pd.read_csv('HS_datasets/jute-exports.txt')
# print(df)

for ind in df.index:
    a = str(df['Year'][ind])
    b = df['Exports'][ind]
    #print(a,b)
    x.append(a)
    y.append(b)
      
plt.title("Jute exports")
plt.xlabel('Year')
plt.ylabel('Total Value (in crore)')
#plt.yticks(y)
plt.plot(x, y)
  
plt.savefig('HS_datasets/jute.png')