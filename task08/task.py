# 1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата
# «день-месяц-год». В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать
# число, месяц, год и преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить
# валидацию числа, месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных
# данных.

# class Date:
#     def __init__(self, data: str):
#         self.data = data.split('-')
#
#     @classmethod
#     def to_type(cls, date_str: str) -> str:
#         try:
#             day, month, year = [int(i) for i in date_str.split('-')]
#             return f"{type(day), day} {type(month), month} {type(year), year}"
#         except ValueError:
#             return 'Указана неправильная дата!'
#
#     @staticmethod
#     def is_valid(date_str: str) -> str:
#         try:
#             day, month, year = [int(i) for i in date_str.split('-')]
#             valid_text = Date.__validate(day, month, year)
#             if valid_text is None:
#                 return 'Ok'
#             return valid_text
#         except ValueError:
#             return 'Указана неправильная дата!'
#
#     @classmethod
#     def __validate(cls, day: int, month: int, year: int) -> str:
#         print(f'{day} {month} {year}')
#         if day > 31 or day < 1:
#             return f'Error day {day} is not valid'
#         if month > 12 or month < 1:
#             return f'Error month {month} is not valid.'
#         return None
#
#
# print(Date.is_valid('25-12-2021'))
# print(Date.is_valid('32-12-2021'))
# print(Date.is_valid('30-22-2021'))
# print(Date.to_type('31-12-2021'))


# 2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль. Проверьте его работу на данных,
# вводимых пользователем. При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту
# ситуацию и не завершиться с ошибкой.

# class DivideException(BaseException):
#     def __init__(self, txt):
#         self.txt = txt
#
#
# try:
#     user_num_1 = int(input('Введите делимое: '))
#     user_num_2 = int(input('Введите делитель: '))
#     if user_num_2 == 0:
#         raise DivideException("Делить на ноль нельзя!")
#     else:
#         res = user_num_1 / user_num_2
# except ValueError:
#     print("Вы ввели не число")
# except DivideException:
#     print('DivideException: деление на 0')


# 3. Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел.
# Проверить работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и заполнять список
# только числами. Класс-исключение должен контролировать типы данных элементов списка.
# Примечание: длина списка не фиксирована. Элементы запрашиваются бесконечно, пока пользователь сам не остановит
# работу скрипта, введя, например, команду “stop”. При этом скрипт завершается, сформированный список с числами
# выводится на экран. Подсказка: для данного задания примем, что пользователь может вводить только числа и строки.
# При вводе пользователем очередного элемента необходимо реализовать проверку типа элемента и вносить его в список,
# только если введено число. Класс-исключение должен не позволить пользователю ввести текст (не число) и отобразить
# соответствующее сообщение. При этом работа скрипта не должна завершаться.

# class Type_error_list:
#     def __init__(self, *args):
#         self.my_list = []
#
#     def input(self):
#         while True:
#             try:
#                 val = int(input('Введите значения и нажимайте Enter - '))
#                 self.my_list.append(val)
#                 print(f'Текущий список - {self.my_list} \n ')
#             except:
#                 print(f"Недопустимое значение - строка и булево")
#                 y_or_n = input(f'Попробовать еще раз? Y/N ')
#
#                 if y_or_n == 'Y' or y_or_n == 'y':
#                     print(try_except.my_input())
#                 elif y_or_n == 'N' or y_or_n == 'n':
#                     return f'Вы вышли'
#                 else:
#                     return f'Вы вышли'
#
#
# Type_error_list = Type_error_list(1)
# print(Type_error_list.input())


# 4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника»,
# который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер,
# ксерокс). В базовом классе определить параметры, общие для приведенных типов. В классах-наследниках реализовать
# параметры, уникальные для каждого типа оргтехники.

# 5. Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на склад и передачу в
# определенное подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники,
# а также других данных, можно использовать любую подходящую структуру, например словарь.

# 6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных. Например,
# для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
#
# Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей, изученных на
# уроках по ООП.

# class Equipment:
#     def __init__(self, id: int, model: str, price: float):
#         self._model = model
#         self._price = price
#         self.__id = id
#
#     def run(self, file_name: str, count: int = 1):
#         return ''
#
#     def get_description(self) -> str:
#         return f'Model: {self._model}, price: {self._price}, id: {self.__id}'
#
#
# class Printer(Equipment):
#     def run(self, file_name: str, count: int = 1):
#         return f'Устройство {self._model}: Печатаем документ {file_name} в количестве {count} копии'
#
#
# class Scanner(Equipment):
#
#     def run(self, file_name: str, count: int = 1):
#         return f'Устройство {self._model}: Сканируем документ {file_name} в количестве {count} копии'
#
#
# class Copier(Equipment):
#
#     def run(self, file_name: str, count: int = 1):
#         return f'Устройство {self._model}: Копируем документ {file_name} в количестве {count} копии'
#
#
# class StorageEquipment:
#     _id: int
#     _name: str
#     _address: str
#     _equipment: list
#
#     def __init__(self, id: int, name: str, address: str):
#         self._name = name
#         self._address = address
#         self._id = id
#         self._equipment = []
#
#     def get_id(self):
#         return self._id
#
#     def get_name(self):
#         return self._name
#
#     def get_address(self):
#         return self._address
#
#     def get_equipments(self):
#         return self._equipment
#
#     def get_len_equipments(self):
#         return len(self._equipment)
#
#     def get_len_equipment(self, equipment: Equipment):
#         return self._equipment.count(equipment)
#
#     def get_equipment(self, id: int):
#         return self._equipment[id]
#
#     def add_equipment(self, equipment: Equipment):
#         self._equipment.append(equipment)
#
#     def remove_equipment(self, equipment: Equipment):
#         self._equipment.remove(equipment)
#
#
# class Storages:
#     _storages: dict = {}
#
#     def add_storage(self, storage: StorageEquipment):
#         self._storages[storage.get_id()] = storage
#
#     def get_storage(self, id: int) -> StorageEquipment:
#         return self._storages[id]
#
#     def get_storages(self) -> list:
#         storages = {}
#         for id in self._storages:
#             storage = self._storages[id]
#             storages[id] = {storage.get_id(), storage.get_name(), storage.get_address(), storage.get_equipments()}
#         return storages
#
#     def get_storage_info(self) -> str:
#         result = ''
#         for id in self._storages:
#             storage = self._storages[id]
#             result = result + f'[id: {storage.get_id()} ({storage.get_name()})]'
#         return result
#
#     def move_equipment_to(self, fromStorage: StorageEquipment, toStorage: StorageEquipment, equipment: Equipment,
#                           count: int = 1):
#         i = 0
#         while i < count:
#             fromStorage.remove_equipment(equipment)
#             toStorage.add_equipment(equipment)
#             i = i + 1
#
#
# # создаем различные типы оборудования
# scanner01 = Scanner(1, 'Scaner Canon MX', 3500.0)
# scanner02 = Scanner(2, 'Scaner Canon RX', 8500.0)
# scanner03 = Scanner(3, 'Scaner Canon XX', 13500.0)
#
# copier01 = Copier(4, 'Copier Canon MX', 3500.0)
# copier02 = Copier(5, 'Copier Canon MX', 3500.0)
# copier03 = Copier(6, 'Copier Canon XX', 13500.0)
#
# printer01 = Printer(7, 'Printer Canon MX', 3500.0)
# printer02 = Printer(8, 'Printer Canon RX', 8500.0)
# printer03 = Printer(9, 'Printer Canon XX', 13500.0)
#
# # создаем склады
# storage01 = StorageEquipment(1, 'Склад 1', 'Адресс склада 1')
# storage02 = StorageEquipment(2, 'Склад 2', 'Адресс склада 2')
# storage03 = StorageEquipment(3, 'Склад 3', 'Адресс склада 3')
#
# # создаем класс для управления складами и добавляем в него созданные склады
# storages = Storages()
# storages.add_storage(storage01)
# storages.add_storage(storage02)
# storages.add_storage(storage03)
#
# # добавляем оборудования на склад по ID номеру
# storages.get_storage(1).add_equipment(scanner01)
# storages.get_storage(1).add_equipment(scanner01)
# storages.get_storage(1).add_equipment(scanner01)
#
# storages.get_storage(2).add_equipment(scanner02)
# storages.get_storage(2).add_equipment(scanner03)
# storages.get_storage(2).add_equipment(printer01)
# storages.get_storage(2).add_equipment(printer02)
# storages.get_storage(2).add_equipment(printer02)
# storages.get_storage(2).add_equipment(printer02)
# storages.get_storage(2).add_equipment(printer03)
#
# storages.get_storage(3).add_equipment(copier01)
# storages.get_storage(3).add_equipment(copier02)
# storages.get_storage(3).add_equipment(copier03)
# storages.get_storage(3).add_equipment(copier03)
# storages.get_storage(3).add_equipment(copier03)
# storages.get_storage(3).add_equipment(scanner01)

# # выводим подробный список того, что имееется на складах
# for index in [1, 2, 3]:
#     print(f'На складе {index} хранится  {storages.get_storage(index).get_len_equipments()} штук продукции:')
#     for i in storages.get_storage(index).get_equipments():
#         print(i.get_description())
#
# # выводим количество оборудования на складах
# print(f'Сколько хранится {scanner01.get_description()} на складе {storages.get_storage(1).get_name()}:')
# print(f'{storages.get_storage(1).get_len_equipment(scanner01)}')
#
# print(f'Сколько хранится {scanner01.get_description()} на складе {storages.get_storage(2).get_name()}:')
# print(f'{storages.get_storage(2).get_len_equipment(scanner01)}')
#
# print(f'Сколько хранится {scanner01.get_description()} на складе {storages.get_storage(3).get_name()}:')
# print(f'{storages.get_storage(3).get_len_equipment(scanner01)}')
#
# # Перемещаем товавы между складами
# storages.move_equipment_to(storage01, storage02, scanner01, 3)
# storages.move_equipment_to(storage02, storage03, scanner01, 1)
# storages.move_equipment_to(storage03, storage01, scanner01, 1)
# # Проверяем
# print('--------------------')
#
# print(f'Сколько хранится {scanner01.get_description()} на складе {storages.get_storage(1).get_name()}:')
# print(f'{storages.get_storage(1).get_len_equipment(scanner01)}')
#
# print(f'Сколько хранится {scanner01.get_description()} на складе {storages.get_storage(2).get_name()}:')
# print(f'{storages.get_storage(2).get_len_equipment(scanner01)}')
#
# print(f'Сколько хранится {scanner01.get_description()} на складе {storages.get_storage(3).get_name()}:')
# print(f'{storages.get_storage(3).get_len_equipment(scanner01)}')
#
# print('--------------------')
# print(f'Для выхода - Q, продолжение - Enter')
# while True:
#     try:
#         type = int(input(f'Введите тип устройства 1 - сканер, 2 принтер, 3 ксерокс >>> '))
#         id = int(input(f'Введите Id устройства >>> '))
#         name = str(input(f'Введите модель устройства >>> '))
#         price = float(input(f'Стоимость устройства >>> '))
#         storage_id = int(input(f'На какой склад отправить [id]? {storages.get_storage_info()} >>> '))
#
#         if type == 1:
#             equipment = Scanner(id, name, price)
#             storages.get_storage(storage_id).add_equipment(equipment)
#             print(f'Текущий список -\n {storages.get_storage(storage_id).get_equipments()}')
#         elif type == 2:
#             equipment = Printer(id, name, price)
#             storages.get_storage(storage_id).add_equipment(equipment)
#             print(f'Текущий список -\n {storages.get_storage(storage_id).get_equipments()}')
#         elif type == 3:
#             equipment = Copier(id, name, price)
#             storages.get_storage(storage_id).add_equipment(equipment)
#             print(f'Текущий список -\n {storages.get_storage(storage_id).get_equipments()}')
#         else:
#             print(f'Ошибка, данного типа не существует')
#
#     except:
#         print(f'Ошибка ввода данных')
#
#     print(f'Для выхода - Q, продолжение - Enter')
#     q = input(f'---> ')
#     if q == 'Q' or q == 'q':
#         print(f'Выход')
#         break

# 7. Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число», реализуйте перегрузку
# методов сложения и умножения комплексных чисел. Проверьте работу проекта, создав экземпляры класса (комплексные
# числа) и выполнив сложение и умножение созданных экземпляров. Проверьте корректность полученного результата.

# class ComplexNumber:
#     def __init__(self, a, b, ):
#         self.a = a
#         self.b = b
#         self.z = 'a + b'
#
#     def __add__(self, other):
#         print(f'Сумма z1 и z2 равна')
#         return f'z = {self.a + other.a} + {self.b + other.b}'
#
#     def __mul__(self, other):
#         print(f'Произведение z1 и z2 равно')
#         return f'z = {self.a * other.a - (self.b * other.b)} + {self.b * other.a}'
#
#     def __str__(self):
#         return f'z = {self.a} + {self.b} '
#
#
# z_1 = ComplexNumber(1, -2)
# z_2 = ComplexNumber(3, 4)
# print(z_1)
# print(z_1 + z_2)
# print(z_1 * z_2)
