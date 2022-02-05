

class Date:
    def __init__(self, str_date):
        self.str_date = str_date

    @classmethod
    def type_number(cls, str_date):
        day, month, year = [int(i) for i in str_date.split('-')]
        print(f'день {type(day)} - {day}\nмесяц {type(month)} - {month}\nгод {type(year)} - {year}')

    @staticmethod
    def valid_number(str_date):
        try:

            day, month, year = str_date.split('-')

            day = int(day)
            month = int(month)
            year = int(year)

            if month > 12 or month < 1:
                raise TypeError('Не правельно введен месяц')
            if day > 31 or day < 1:
               raise TypeError('Не правильно введена дата')
            if year < 1000:
                raise TypeError('Не правильно введен год')

            if month in [4, 6, 9, 11] and day == 31:
                raise TypeError('Не правильно введена дата')

            if (month == 2 and day == 29 and year % 4 != 0 and
                year % 100 != 0 and year % 400 != 0):
                raise TypeError('Не правильно введена дата')
            if (month == 2 and day > 29):
                raise TypeError('Не правильно введена дата')
            
        except ValueError:
            print('Данные введены не правильном формате')
        except TypeError as error:
            print(error)

dat = '30-02-2021'      

Date.type_number(dat)

Date.valid_number(dat)


