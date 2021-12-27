

list_1 = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

list_2 = []


for i in list_1:
    if i.isdigit():
        list_2.append('"{:02}"'.format(int(i)))
    elif i.startswith('+'):
        list_2.append('"{}{:02}"'.format(i[0], int(i)))
    elif i.startswith('-'):
        list_2.append('"{}{:02}"'.format(i[0], int(i[1])))
    else:
        list_2.append(i)

print(' '.join(list_2))
