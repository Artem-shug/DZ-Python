

import os


direct= 'work'

limit_list = [100, 1000, 10000, 100000]
size_list = []

for root, dirs, files in os.walk(direct):
    for file in files:
        path = os.path.join(root, file)
        size = os.path.getsize(path)
        size_list.append(size)

list_1 = [size for size in size_list if size < 100]
list_2 = [size for size in size_list if 100 <= size <= 1000]
list_3 = [size for size in size_list if 1000 < size <= 10000]
list_4 = [size for size in size_list if size > 100000]
res = [len(list_1), len(list_2), len(list_3), len(list_4)]

result = dict(zip(limit_list, res))

print(result)

