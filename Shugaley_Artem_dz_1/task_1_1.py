

duration = int(input('Введите количество секунд: '))
n = duration

s = n % 60
m = (n // 60) % 60
h = (n // 3600) % 24
d = n // 86400


if n < 60:
    print('{} сек'.format(s))
elif 60 <= n < 3600:
    print('{} мин. {} сек'.format(m, s))
elif 3600 <= n < 86400:
    print('{} час {} мин {} сек'.format(h, m, s))
else:
    print('{} дн {} час {} мин {} сек'.format(d, h, m, s))