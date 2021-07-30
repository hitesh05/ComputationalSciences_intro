import pandas as pd
import re

df = pd.read_csv('project.csv')

# congress_count = 0
# congress_cases = 0
# bjp_count = 0
# bjp_cases = 0
# cpi_count = 0
# cpi_cases = 0

# for ind in df.index:
#     if df['Party'][ind] == 'INC':
#         congress_count += 1
#         congress_cases += df['Criminal Cases'][ind]
#     if df['Party'][ind] == 'BJP':
#         bjp_count += 1
#         bjp_cases += df['Criminal Cases'][ind]
#     if df['Party'][ind] == 'CPI(M)':
#         cpi_count += 1
#         cpi_cases += df['Criminal Cases'][ind]
#     if df['Party'][ind] == 'CPI':
#         cpi_count += 1
#         cpi_cases += df['Criminal Cases'][ind]

# a = congress_cases / congress_count
# b = bjp_cases / bjp_count
# c = cpi_cases / cpi_count

# print("Average criminal cases for INC candidates: ", a)
# print("Average criminal cases for BJP candidates: ", b)
# print("Average criminal cases for LDF candidates: ", c)

income = df['Assets'][3]
# print(income)
# print(type(income))
# temp = re.findall(r'\b\d+\b', income)
# # print(temp)
# res = list(map(int, temp))

# # res = [int(i) for i in income.split() if i.isdigit()]
# print(res)

pattern1 = r'Rs'
pattern2 = r'~'
pattern3 = r'[A-Za-z]+'
pattern4 = r'[+]'
mod_string = re.sub(pattern1, '', income)
mod_string = re.sub(pattern2, '', mod_string)
mod_string = re.sub(pattern3, '', mod_string)
mod_string = re.sub(pattern4, '', mod_string)
mod_string.split()
# print(mod_string)
# res = set(mod_string)
# print(res)
# res = list(map(int,mod_string))
# print(res)

spaces = 0
num = str()
for x in mod_string:
    if x == ' ':
        spaces += 1
    elif spaces == 2:
        break
    else:
        if x == ' ':
            continue
        else:
            num += x

print(num)
