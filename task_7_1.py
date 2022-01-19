
import os


dir_ = os.path.abspath(os.curdir)

dir_1 = input('Введите название проекта ')
dir_2 = input('Введите название папки ')
dir_3 = input('Введите название папки ')
dir_4 = input('Введите название папки ')
dir_5 = input('Введите название папки ')

if not os.path.exists(dir_1):
    os.mkdir(f'{dir_}/{dir_1}')

try:
    os.mkdir(f'{dir_}/{dir_1}/{dir_2}')
    os.mkdir(f'{dir_}/{dir_1}/{dir_3}')
    os.mkdir(f'{dir_}/{dir_1}/{dir_4}')
    os.mkdir(f'{dir_}/{dir_1}/{dir_5}')
except FileExistsError:
    print()

dan = os.walk(dir_1)

for i in dan:
    print(i)

