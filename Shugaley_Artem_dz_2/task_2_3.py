

list_1 = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']


i = 0
while i < len(list_1):
    if list_1[i].isdigit():
        list_1[i] = list_1[i].zfill(2)
        list_1.insert(i, '"')
        list_1.insert(i + 2, '"')
        i += 1
    elif list_1[i].startswith('+') or list_1[i].startswith('-'):
        list_1[i] = list_1[i].zfill(3)
        list_1.insert(i, '"')
        list_1.insert(i + 2, '"')
        i += 1
    i += 1

print(' '.join(list_1))
