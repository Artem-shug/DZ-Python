
import sys
import pickle

with open('users.csv', 'r') as file_1:
    users = file_1.read().replace(',', ' ')
    us = users.splitlines()
    
with open('hobby.csv', 'r') as file_2:
    hobby = file_2.read()
    hob = hobby.splitlines()

if len(us) > len(hob):
    hob.append(None)
elif len(us) < len(hob):
    sys.exit('1')

res_1 = dict(tuple(zip(us, hob)))

print(res_1)

with open('result.csv', 'wb') as file_3:
    pickle.dump(res_1, file_3)

print()

with open('result.csv', 'rb') as file_3:
    result = pickle.load(file_3)

print(result)

