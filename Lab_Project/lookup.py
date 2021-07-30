import pandas as pd
import re

with open('links.csv', 'r') as f:
    text = f.read()
    # text = re.findall(r'http\S+', text)
    text = re.findall(r',\S+http://toi\S+', text)

# with open('Output.csv' , 'w') as f:
#     f.writelines(text)

print(text)