
import requests
from bs4 import BeautifulSoup
from decimal import Decimal
import datetime as dt

URL = 'http://www.cbr.ru/scripts/XML_daily.asp'


response = requests.get(URL)

soup = BeautifulSoup(response.text, 'html.parser')

def currency_rates(x):
    convert_USD = soup.findAll('valute', {'id':'R01235'})
    convert_val_USD = convert_USD[0].value.text
    convert_code_USD = convert_USD[0].charcode.text
    convert_EUR = soup.findAll('valute', {'id':'R01239'})
    convert_val_EUR = convert_EUR[0].value.text
    convert_code_EUR = convert_EUR[0].charcode.text
    convert_CNY = soup.findAll('valute', {'id':'R01375'})
    convert_val_CNY = convert_CNY[0].value.text
    convert_code_CNY = convert_CNY[0].charcode.text
    now = dt.date.today()
    
    if x == convert_code_USD or x == convert_code_USD.lower():
        print(Decimal(convert_val_USD.replace(',','.')), now)
    elif x == convert_code_EUR or x == convert_code_EUR.lower():
        print(Decimal(convert_val_EUR.replace(',','.')), now)
    elif x == convert_code_CNY or x == convert_code_CNY.lower():
        print(Decimal(convert_val_CNY.replace(',','.')), now)
    else:
        print('None')
    return x

if __name__ == '__main__':
    currency_rates('eur')

