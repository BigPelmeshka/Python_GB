# Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево). А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда). Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.

class Car:

    def __init__(self, name, speed, color, is_police=False):
        self.name = name
        self.speed = speed
        self.color = color
        self.is_police = is_police

    def go(self):
        return 'Машина {} на дороге'.format(self.name)

    def stop(self):
        return '\n Машина {} остановилась .'.format(self.name)

    def turn(self, direction):
        return '\n Маштна {} повернула {}'.format(self.name, direction)

    def show_speed(self):
        return '\n Ваша скорость: {}'.format(self.speed)


class TownCar(Car):
    def show_speed(self):
        if self.speed >= 60:
            return '\n Вы превысили допустимый скоростной режим! Ваша скорость: {} км/ч при допустимых 60 км/ч'.format(self.speed)
        else:
            return '\n Ваша скорость в пределах нормы: {} '.format(self.name)


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed >= 40:
            return '\n Вы превысили допустимый скоростной режим! Ваша скорость: {} км/ч при допустимых 40 км/ч'.format(self.speed)
        else:
            return '\n Ваша скорость в пределах нормы: {} '.format(self.name)


class PoliceCar(Car):
    pass


town = TownCar('BMW', 100, 'Черная', False)
print('1:\n' + town.go(), town.show_speed(), town.turn('направо'), town.turn('налево'), town.stop())

sport = SportCar('BMW i8', 10, 'Красная', False)
print('2:\n' + sport.go(), sport.show_speed(), sport.turn('направо'), sport.stop())

work = WorkCar('Копейка', 3, 'Желтая', False)
print('3:\n' + work.go(), work.show_speed(), work.turn('налево'), work.stop())

police = PoliceCar('Лада Веста', 100, 'Синяя', True)
print('4:\n' + police.go(), police.show_speed(), police.turn('налево'), police.stop())