# 1. Определение количества различных подстрок с использованием хэш-функции. Пусть дана строка S длиной N,
# состоящая только из маленьких латинских букв. Требуется найти количество различных подстрок в этой строке.

import hashlib


str_lower = input('Введите строку: ').lower()

hash_set = set()
for i in range(len(str_lower) + 1):
    for j in range(i + 1, len(str_lower) + 1):
        hash_str = hashlib.sha1(str_lower[i:j].encode('utf-8')).hexdigest()
        hash_set.add(hash_str)

print(f'Колличество различных подстрок строке {str_lower} : {len(hash_set)}')
