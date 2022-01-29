

class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color.capitalize()
        self.name = name
        self.is_police = bool(is_police)

    def go(self):
        info_1 = 'поехала'
        return info_1
    def stop(self):
        info_2 = 'остановилась'
        return info_2
    def direction_left(self):
        info_3 = 'повернула на лево'
        return info_3
    def direction_right(self):
        info_4 = 'повернула на право'
        return info_4
    def show_speed(self):
        info_5 = f'текущая скорость автомобиля {self.speed} км/ч'
        return info_5


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
    def show_speed(self):
        if self.speed > 60:
            return 'ПРЕВЫШЕНИЕ СКОРОСТИ !!!'
        else:
            return ''  
    def show(self):
        print(f'{self.show_speed()} {self.color} машина {self.name} движеться со скоростью {self.speed} км/ч')


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
    def show(self):
        print(f'{self.color} {self.name} {self.stop()}. Машина {self.go()}, {self.direction_left()}, {self.show_speed()}')


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
    def show_speed(self):
        if self.speed > 40:
            return 'ПРЕВЫШЕНИЕ СКОРОСТИ !!!'
        else:
            return ''  
    def show(self):
        print(f'{self.show_speed()} {self.color} машина {self.name} движеться со скоростью {self.speed} км/ч')


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
    def show(self):
        print(f'{self.color} {self.name} {self.stop()}. Машина {self.go()}, {self.direction_right()}, {self.show_speed()}')


car_1 = TownCar(85, 'красная', 'audi', False)
car_1.show()

car_2 = SportCar(120, 'белый', 'Mercedes', False)
car_2.show()

car_3 = WorkCar(60, 'черный', 'BMW', False)
car_3.show()    

car_4 = PoliceCar(100, 'серая', 'ВАЗ-2115', True)
car_4.show()

