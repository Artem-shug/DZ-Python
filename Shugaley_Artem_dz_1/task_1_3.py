
for i in range(1, 101):
    if i % 10 == 1 and i % 100 != 11:
        print('{} процент'.format(i))
    elif 1 < i % 10 <= 4 and (i % 100 < 10 or i % 100 > 20):
        print('{} процента'.format(i))
    else:
        print('{} процентов'.format(i))
   
