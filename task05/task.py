# 1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем. Об
# окончании ввода данных свидетельствует пустая строка.
import os
import re
import json

file_name = 'task1.txt'
print(file_name)
try:
    with open(file_name, 'w') as file:
        for str in input('Текст для записи в файл. Для перевода стрки используйте символ *:'):
            file.write(str.replace('*', '\n'))
except IOError:
    print("Произошла ошибка ввода-вывода")

try:
    with open(file_name, 'r') as file:
        for str in file:
            print(str.replace('\n', ''))
except IOError:
    print("Произошла ошибка ввода-вывода")

# os.remove(file_name)

# 2. Создать текстовый файл (не программно), сохранить в нем
# несколько строк, выполнить подсчет количества строк, количества слов в каждой строке.

file_name = 'task2.txt'
try:
    with open(file_name, 'a+') as file:
        list = ['одно\n', 'два слова\n', 'три слова какие-то\n']
        file.writelines(list)
except IOError:
    print("Произошла ошибка ввода-вывода")

try:
    with open(file_name, 'r') as file:
        print(file_name)
        for str in file.readlines():
            str = str.replace('\n', '')
            print(f"Строка : {str} \nКолличество слов {len(str.split(' '))}")
except IOError:
    print("Произошла ошибка ввода-вывода")

# os.remove(file_name)

# 3. Создать текстовый файл (не
# программно), построчно записать фамилии сотрудников и величину их окладов (не менее 10 строк). Определить,
# кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников. Выполнить подсчет средней величины
# дохода сотрудников.
#
# Пример файла:
#
# Иванов 23543.12
# Петров 13749.32

file_name = 'task3.txt'
try:
    with open(file_name, 'r') as file:
        print(f"Сотрудники с окладом менее 20 000:")
        count = 0;
        sum_sallary = 0;
        for str in file.readlines():
            list = str.split(' ')
            if float(list[1]) < 20000:
                print(str.replace('\n', ''))
            count += 1
            sum_sallary += float(list[1])
        print(f"Средний оклад:  {sum_sallary / count}")
except IOError:
    print("Произошла ошибка ввода-вывода")

# os.remove(file_name)

# 4. Создать (не программно) текстовый файл со следующим содержимым:
#
# One — 1 Two — 2 Three — 3 Four — 4 Необходимо написать программу, открывающую файл на чтение и считывающую
# построчно данные. При этом английские числительные должны заменяться на русские. Новый блок строк должен
# записываться в новый текстовый файл.

file_name = 'task4.txt'
file_name_new = 'task4_new.txt'
dict = {'One': 'один', 'Two': 'два', 'Three': 'три', 'Four': 'четыри'}

new_str_list = []
try:
    with open(file_name, 'r') as file:
        for str in file.readlines():
            for i in dict.items():
                if str.find(i[0]) >= 0:
                    new_str_list.append(str.replace(i[0], i[1]))
except IOError:
    print("Произошла ошибка ввода-вывода")

try:
    with open(file_name_new, 'w+') as file:
        file.writelines(new_str_list)
except IOError:
    print("Произошла ошибка ввода-вывода")

# os.remove(file_name)
# os.remove(file_name_new)

# 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами. Программа
# должна подсчитывать сумму чисел в файле и выводить ее на экран.

file_name = 'task5.txt'
try:
    with open(file_name, 'w') as file:
        file.writelines([str(i) + ' ' for i in range(10, 100, 10)])
except IOError:
    print("Произошла ошибка ввода-вывода")

try:
    sum = 0
    with open(file_name, 'r') as file:
        list_source = file.readlines()
        for list in list_source:
            for num in list.split(' '):
                if (len(num) > 0):
                    sum += int(num)
        print(f"Сума чисел: {sum}")
except IOError:
    print("Произошла ошибка ввода-вывода")

# os.remove(file_name)

# 6. Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие
# лекционных, практических и лабораторных занятий по этому предмету и их количество. Важно, чтобы для каждого
# предмета не обязательно были все типы занятий. Сформировать словарь, содержащий название предмета и общее
# количество занятий по нему. Вывести словарь на экран.
#
# Примеры строк файла: Информатика: 100(л) 50(пр) 20(лаб).
# Физика: 30(л) — 10(лаб)
# Физкультура: — 30(пр) —
# Пример словаря: {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}

file_name = 'task6.txt'
dict = {}
try:
    with open(file_name, 'r') as file:
        for line in file.readlines():
            name, string = line.split(':')
            sum_hours = 0
            for str in string.split():
                numbers = re.split('\D+', str)
                for num in numbers:
                    if num.isnumeric():
                        sum_hours += int(num)
            dict[name] = sum_hours
        print(f'Общее количество часов по предмету - \n {dict}')
except IOError:
    print("Произошла ошибка ввода-вывода")
# os.remove(file_name)

# 7. Создать вручную и заполнить несколькими строками текстовый файл, в котором каждая строка должна содержать данные
# о фирме: название, форма собственности, выручка, издержки.
#
# Пример строки файла: firm_1 ООО 10000 5000. Необходимо построчно прочитать файл, вычислить прибыль каждой компании,
# а также среднюю прибыль. Если фирма получила убытки, в расчет средней прибыли ее не включать. Далее реализовать
# список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью. Если фирма
# получила убытки, также добавить ее в словарь (со значением убытков).
#
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
#
# Пример json-объекта:
#
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
#
# Подсказка: использовать менеджер контекста.

file_name = 'task7.txt'
file_name_new = 'task7_json.txt'
profit = {}
pr = {}
prof = 0
prof_aver = 0
i = 0
with open(file_name, 'r') as file:
    for line in file:
        name, firm, earning, damage = line.split()
        profit[name] = int(earning) - int(damage)
        if profit.setdefault(name) >= 0:
            prof = prof + profit.setdefault(name)
            i += 1
    if i != 0:
        prof_aver = prof / i
        print(f'Прибыль средняя - {prof_aver:.2f}')
    else:
        print(f'Прибыль средняя - отсутсвует. Все работают в убыток')
    pr = {'средняя прибыль': round(prof_aver)}
    profit.update(pr)
    print(f'Прибыль каждой компании - {profit}')

with open('file_7.json', 'w') as write_js:
    json.dump(profit, write_js)

    js_str = json.dumps(profit)
    print(f'Создан файл с расширением json со следующим содержимым: \n '
          f' {js_str}')

# os.remove(file_name)
# os.remove(file_name_new)