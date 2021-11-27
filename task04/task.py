from functools import reduce
from itertools import cycle, count
from typing import Tuple, List


def print_log_info(type_id: int, number: int) -> None:
    str_start = 'Задание ' + str(number)

    if type_id == 1:
        str_end = '***Начало***'
    else:
        str_end = '***Конец***'
    print(f"{str_start}: \r\n {str_end}")


index = 1

# 1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
# В расчете необходимо использовать формулу: (выработка в часах*ставка в час) + премия.
# Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.

print_log_info(1, index)


def task_1_calc_salary(hours: int, rate_per_hour: float, bonus: float = 0.0, currency: str = 'Руб') -> None:
    salary = (hours * rate_per_hour) + bonus
    print(f"Заработная плата сотрудника: {salary} {currency}")


task_1_calc_salary(20, 300)
task_1_calc_salary(1, 105.5, 5000, 'Euur')

print_log_info(0, index)
index += 1

# 2. Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего
# элемента.
#
# Подсказка: элементы, удовлетворяющие условию, оформить в виде списка. Для формирования списка использовать генератор.
# Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
# Результат: [12, 44, 4, 10, 78, 123].

print_log_info(1, index)


def task_2_generate_data_list() -> Tuple[List[int], List[int]]:
    list_result = []
    list_source = [int(i) for i in input("Введите список чисел через запятую: ").split(',')]
    for i in range(1, len(list_source)):
        if list_source[i] > list_source[i - 1]:
            (list_result.append(list_source[i]))
    return list_result, list_source


list_result, list_source = task_2_generate_data_list()
print(f"Исходный лист: {list_source}")
print(f"Отформатированный лист: {list_result}")

print_log_info(0, index)
index += 1

# 3. Для чисел в пределах от 20 до 240 найти числа, кратные 20 или 21. Необходимо решить задание в одну строку.
# Подсказка: использовать функцию range() и генератор.
print_log_info(1, index)


def task_3_get_multiplicity_list(start_range: int = 20, end_range: int = 240) -> None:
    list = [i for i in range(start_range, end_range) if i % 20 == 0 or i % 21 == 0]
    print(f"Список чисел кратных 20 или 21 в диапазоне [{start_range}..{end_range}): ", list)


task_3_get_multiplicity_list()

print_log_info(0, index)
index += 1

# 4. Представлен список чисел. Определить элементы списка, не имеющие повторений.
# Сформировать итоговый массив чисел, соответствующих требованию.
# Элементы вывести в порядке их следования в исходном списке.
# Для выполнения задания обязательно использовать генератор.
#
# Пример исходного списка: [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11].
# Результат: [23, 1, 3, 10, 4, 11]
print_log_info(1, index)


def task_4_get_unique_list(List: List) -> List[int]:
    return [i for i in List if List.count(i) == 1]


list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
print("Исходные элементы списка:\n", list)
list = task_4_get_unique_list(list)
print("Элементы списка, не имеющие повторений:\n", list)
print_log_info(0, index)
index += 1

# 5. Реализовать формирование списка, используя функцию range() и возможности генератора. В список должны войти
# четные числа от 100 до 1000 (включая границы). Необходимо получить результат вычисления произведения всех элементов
# списка.
#
# Подсказка: использовать функцию reduce().
print_log_info(1, index)


def task_5_get_generate_list(start: int = 100, end: int = 1000, step: int = 2) -> Tuple[List[int], int, int, int]:
    source_list = [i for i in range(start, end + 1, step)]
    result_list = reduce(lambda x, y: x * y, source_list)
    return source_list, result_list, start, end


source_list, result_list, start, end = task_5_get_generate_list()
print(f"Список чётных чисел в диапазоне [{start}..{end}]:\n", source_list)
print("Произведение всех элементов списка:\n", result_list)

print_log_info(0, index)
index += 1

# 6. Реализовать два небольших скрипта:
#
# а) итератор, генерирующий целые числа, начиная с указанного,
# б) итератор, повторяющий элементы некоторого списка, определенного заранее.
#
# Подсказка: использовать функцию count() и cycle() модуля itertools. Обратите внимание, что создаваемый цикл не
# должен быть бесконечным. Необходимо предусмотреть условие его завершения. Например, в первом задании выводим целые
# числа, начиная с 3, а при достижении числа 10 завершаем цикл. Во втором также необходимо предусмотреть условие,
# при котором повторение элементов списка будет прекращено.
print_log_info(1, index)

print("Итератор, генерирующий целые числа, начиная с указанного:")
for i in count(3):
    if i > 10:
        break
    else:
        print(i)
    i += 1

print("Итератор, повторяющий элементы некоторого списка, определенного заранее:")
j = 0
for i in cycle([1, 2, 3, 4, 5, 6]):
    if j > 10:
        break
    print(i)
    j += 1


print_log_info(0, index)
index += 1

# 7. Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение. При вызове
# функции должен создаваться объект-генератор. Функция должна вызываться следующим образом: for el in fact(n).
# Функция отвечает за получение факториала числа, а в цикле необходимо выводить только первые n чисел, начиная с 1! и
# до n!.
#
# Подсказка: факториал числа n — произведение чисел от 1 до n. Например, факториал четырёх 4! = 1 * 2 * 3 * 4 = 24.
print_log_info(1, index)


def task_7_fact(n: int):
    value = 1
    for i in range(1, n + 1):
        value *= i
        yield value


i = 1
for value in task_7_fact(4):
    print(f'факториал числа ({i}): {value}')
    i += 1


print_log_info(0, index)