

import time


class TrafficLight:
    def __init__(self, red, yellow, green):
        self.__red = red
        if self.__red != 'красный':
            quit('Несовпадает порядок режимов')
        self.__yellow = yellow
        if self.__yellow != 'желтый':
            quit('Несовпадает порядок режимов')
        self.__green = green
        if self.__green != 'зеленый':
            quit('Несовпадает порядок режимов')

    def running(self):
        while True:
            print(f'горит {self.__red}')
            time.sleep(7)
            print(f'горит {self.__yellow}')
            time.sleep(2)
            print(f'горит {self.__green}')
            time.sleep(10)
            print()

color = TrafficLight('красный', 'желтый', 'зеленый')

color.running()

