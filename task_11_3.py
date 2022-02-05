

class Spisok(Exception):
    def __init__(self, txt):
        self.txt = txt
    
spisok = []
   
while True:
    try:
        dan = input('Введите данные: ')
        if dan == 'stop':
            break
        elif dan.isdigit() == True:
            spisok.append(int(dan))
        elif dan.isdigit() == False:
            raise Spisok('ВВЕДИТЕ ЧИСЛО !!!')
    except Spisok as error:
        print(error)

print(spisok)
        
