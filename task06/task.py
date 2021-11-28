# 1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
# Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы: красный, желтый,
# зеленый. Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды,
# третьего (зеленый) — на ваше усмотрение. Переключение между режимами должно осуществляться только в указанном
# порядке (красный, желтый, зеленый). Проверить работу примера, создав экземпляр и вызвав описанный метод. Задачу
# можно усложнить, реализовав проверку порядка режимов, и при его нарушении выводить соответствующее сообщение и
# завершать скрипт.
from time import sleep


class TrafficLight:
    __color: str
    color_dict: dict
    yellow_traffic_light: int
    green_traffic_light: int

    def __init__(self, color_dict: dict):
        self.color_dict = color_dict

    def __set_color(self, color: str):
        self.__color = color

    def running(self) -> None:
        for color in self.color_dict.values():
            self.__set_color(color.get('color'))
            print(f"Включен \"{self.__color}\" сигнал светофора на {color.get('time')} секунд ...")
            sleep(int(color.get('time')))
        print(f"Светофор прекратил свою работу")


color_dict = {
    1: {'color': 'Красный', 'time': 7},
    2: {'color': 'Желтый', 'time': 2},
    3: {'color': 'Зеленый', 'time': 10},
}

trafficLight = TrafficLight(color_dict)
trafficLight.running()


# 2. Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина). Значения данных
# атрибутов должны передаваться при создании экземпляра класса. Атрибуты сделать защищенными. Определить метод
# расчета массы асфальта, необходимого для покрытия всего дорожного полотна. Использовать формулу: длина*ширина*масса
# асфальта для покрытия одного кв метра дороги асфальтом, толщиной в 1 см*число см толщины полотна. Проверить работу
# метода. Например: 20м*5000м*25кг*5см = 12500 т

class Road:
    _lenght: int
    _width: int

    def __init__(self, length: int, width: int):
        self._lenght = length
        self._width = width

    def calc_mass_road(self, mass: float, height: float) -> float:
        return self._width * self._lenght * mass * height / 1000


road = Road(20, 5000)
print(f"Массы асфальта, необходимого для покрытия всего дорожного полотн составляет {road.calc_mass_road(25, 5)}")


# 3. Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность),
# income (доход). Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и
# премия, например, {"wage": wage, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker. В
# классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учетом премии (
# get_total_income). Проверить работу примера на реальных данных (создать экземпляры класса Position,
# передать данные, проверить значения атрибутов, вызвать методы экземпляров).

class Worker:
    name: str
    surname: str
    position: str
    _income: dict

    def __init__(
            self,
            name: str,
            surname: str,
            position: str,
            wage: float,
            bonus: float
    ):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}


class Position(Worker):

    def get_full_name(self):
        return self.name + ' ' + self.surname

    def get_full_salary(self):
        return self._income['wage'] + self._income['bonus']


position = Position('Name', 'Surname', 'Worker', 200, 50.50)
print(f'get_full_name: {position.get_full_name()}')
print(f'get_full_salary: {position.get_full_salary()}')

# 4.Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (
# булево). А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась,
# повернула (куда). Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый
# класс метод show_speed, который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar
# переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться
# сообщение о превышении скорости.

class Car:
    name: str
    speed: float
    color: str
    is_police: bool

    def __init__(self, name: str, speed: float, color: str, is_police: bool = False):
        self.name = name
        self.speed = speed
        self.color = color
        self.is_police = is_police

    def go(self):
        return f'Автомобиль {self.name} Автомобиль двигается'

    def stop(self):
        return f'Автомобиль {self.name} остановился'

    def turn(self, direction: str):
        return f'Автомобиль {self.name} повернул {direction}'

    def show_speed(self):
        return f'Ваша скорость {self.speed}'


class TownCar(Car):
    __correct_speed: float = 60

    def show_speed(self):
        if self.speed > self.__correct_speed:
            return f'Скорость {self.speed}, разрешеная {self.__correct_speed}'
        else:
            return f'Ваша скорость {self.speed}'


class SportCar(Car):
    pass


class WorkCar(Car):
    __correct_speed: float = 60

    def show_speed(self):
        if self.speed > self.__correct_speed:
            return f'Скорость {self.speed}, разрешеная {self.__correct_speed}'
        else:
            return f'Ваша скорость {self.speed}'


class PoliceCar(Car):
    pass


townCar = TownCar('Audi', 50, 'blue', False)
print('TownCar:' + townCar.go(), townCar.show_speed(), townCar.turn('налево'), townCar.turn('направо'), townCar.stop())
townCar = TownCar('Audi', 70, 'blue', False)
print('TownCar:' + townCar.go(), townCar.show_speed(), townCar.turn('налево'), townCar.turn('направо'), townCar.stop())

sportCar = SportCar('AudiRS', 170, 'red', False)
print('SportCar:' + sportCar.go(), sportCar.show_speed(), sportCar.turn('налево'), sportCar.turn('направо'),
      sportCar.stop())

workCar = WorkCar('WAZ', 30, 'red', False)
print('WorkCar:' + workCar.go(), workCar.show_speed(), workCar.turn('налево'), workCar.turn('направо'), workCar.stop())
workCar = WorkCar('WAZ', 130, 'red', False)
print('WorkCar:' + workCar.go(), workCar.show_speed(), workCar.turn('налево'), workCar.turn('направо'), workCar.stop())

policeCar = PoliceCar('Kia', 100, 'yellow', True)
print('PoliceCar:' + policeCar.go(), policeCar.show_speed(), policeCar.turn('налево'), policeCar.turn('направо'),
      policeCar.stop())


# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат. 5. Реализовать класс Stationery (канцелярская принадлежность).
# Определить в нем атрибут title (название) и метод draw (отрисовка). Метод выводит сообщение “Запуск отрисовки.”
# Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер). В каждом из классов реализовать
# переопределение метода draw. Для каждого из классов метод должен выводить уникальное сообщение. Создать экземпляры
# классов и проверить, что выведет описанный метод для каждого экземпляра.
class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        return f'Запуск отрисовки'


class Pen(Stationery):
    def draw(self):
        return f'Запуск отрисовки {self.title}'


class Pencil(Stationery):
    def draw(self):
        return f'Запуск отрисовки {self.title}'


class Handle(Stationery):
    def draw(self):
        return f'Запуск отрисовки {self.title}'


pen = Pen('ручкой')
print(pen.draw())
pencil = Pencil('карандашем')
print(pencil.draw())
handle = Handle('маркером')
print(handle.draw())
