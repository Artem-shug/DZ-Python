

from itertools import zip_longest


tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей', 
    'Дмитрий', 'Борис', 'Елена', 'Илья', 'Мария'
]
klasses = [
    '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А'
]

##### 1 способ

res = zip_longest(tutors, klasses)

for i in res:
    print(tuple(i))
print(type(i))

##### через генератор

res = ((tutors[i] , None) if i >= len(klasses) 
    else (tutors[i], klasses[i]) for i in range(len(tutors)))

print(*res, sep='\n')
print(res)

