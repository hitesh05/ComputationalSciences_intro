import pandas as pd
import numpy as np


# Reading the csv file
df_new = pd.read_csv('masterdictdump.csv')

# saving xlsx file
project = pd.ExcelWriter('masterdictdump.xlsx')
df_new.to_excel(project, index = False)

project.save()
