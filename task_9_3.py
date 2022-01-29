

class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}
    
class Position(Worker):
    def get_full_name(self):
        return f'{self.name} {self.surname}'

    def get_total_income(self):
        result = self._income['wage'] + self._income['bonus']
        return result

    def show(self):
        print(f'{self.get_full_name()} работает {self.position} доход {self.get_total_income()} руб.')


user1 = Position('Борис', 'Юрзов', 'железнодорожник', 60000, 5500)
user2 = Position('Анна', 'Зарубина', 'уборщица', 20000, 2250)

user1.show()
user2.show()

