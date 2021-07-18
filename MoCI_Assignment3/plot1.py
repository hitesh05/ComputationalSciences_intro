import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# year = []
# income = []

# f = open('HS_datasets/per-capita.txt','r')

# for row in f:
#     row = row.split(' ')
#     #print(row[0])
#     year.append(row[1])
#     a = int(row[0])
#     b = int(row[2])
#     income.append(b/a)
# f.close()

# plt.bar(year, income, color = 'g')
# # plt.figure(figsize=(10,5))
# # sns.barplot(year, income, alpha=0.8)
  
# plt.xlabel('Year', fontsize = 12)
# plt.ylabel('GDP (per-capita)', fontsize = 13)
  
# plt.title('Increase percentage in GDP', fontsize = 16)
# plt.legend()
# plt.savefig('HS_datasets/gdp.png')
# #plt.show()

year1 = []
exports = []

df = pd.read_csv('HS_datasets/ExportsVsImports.csv')

for ind in df.index:
    a = df['Year'][ind]
    b = df['Exports'][ind]

    year1.append(a)
    exports.append(b)

plt.bar(year1, exports, color = 'b')
  
plt.xlabel('Year', fontsize = 12)
plt.ylabel('Exports as a percentage of imports', fontsize = 13)
  
plt.title('Exports vs Imports', fontsize = 16)
plt.savefig('HS_datasets/ExportsVsImports.png')
#plt.show()