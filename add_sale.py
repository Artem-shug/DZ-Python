
import sys
import csv 

command = sys.argv[1]

with open('bakery.txt', 'a') as file:
    file.write('{}\n'.format(command))
    
with open('bakery.txt', 'r') as file:
    res = file.read()
    res_1 = res.splitlines()
    res_2 = ' '.join(res_1)
    res_3 = res_2.split(' ')
    num = list(enumerate(res_3, 1))
    num_1 = dict(num)

with open('bakery.csv', 'w', encoding='utf-8') as file_2:
    writer = csv.writer(file_2)

    for i in num_1:
        writer.writerow((i, num_1[i]))


    
