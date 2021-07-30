import twint
import csv

csvfile = open('Sabarimala.csv')

# print([x[7] for x in csv.reader(csvfile)])

#userx = [x[0] for x in csv.reader(csvfile)]




c = twint.Config()
count = 0
for x in csv.reader(csvfile):
    if count == 0:
        continue
    else:
        c.Username = x[7]
        twint.run.Lookup(c)
        if User.verified:
            print(c.Username)
        count += 1


# c.User_full = True
# c.Output = "verified.csv"
# c.Store_csv = True



# users = twint.output.users_list
