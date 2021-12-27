

price = [57.8, 46.51, 97, 118.15, 73.6, 60, 39.79, 256.91, 92.35, 70, 156.6]


for i in price:
    r = int(i)
    kk = round((i - r) * 100)
    print('{} руб {:02} коп'.format(r, kk), end=', ')
print(id(price))


price.sort()
for i in price:
    r = int(i)
    kk = round((i - r) * 100)
    print('{} руб {:02} коп'.format(r, kk), end=', ')
print(id(price))


price_1 = list(reversed(price))
for i in price_1:
    r = int(i)
    kk = round((i - r) * 100)
    print('{} руб {:02} коп'.format(r, kk), end=', ')
print(id(price_1))


price_max = price_1[:5]
for i in price_max:
    r = int(i)
    kk = round((i - r) * 100)
    print('{} руб {:02} коп'.format(r, kk), end=', ')
print(id(price_max))

