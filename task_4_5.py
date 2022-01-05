

import sys
from task_4_3 import currency_rates


command = sys.argv[1]

if command == 'USD'or command == 'usd':
    currency_rates('USD')
elif command == 'EUR' or command == 'eur':
    currency_rates('EUR')
elif command == 'CNY' or command == 'cny':
    currency_rates('CNY')
else:
    print('None')

