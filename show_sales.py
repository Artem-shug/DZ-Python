
import csv


with open('bakery.csv') as file:
    reader = csv.reader(file)
    res = [row for row in reader]
    
dict_1 = {}

for i in res:
    dict_1[i[0]] = i[1]

print(dict_1['1'])
for val in dict_1.values():
    print(val) 
