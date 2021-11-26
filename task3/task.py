# 1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
def division(num1, num2):
    try:
        return num1 / num2
    except ZeroDivisionError:
        return 'Деление на 0'
    except ValueError:
        return num1 + ' / ' + num2 + ' не корректно'


while True:
    result = division(int(input('Введите число 1: ')), int(input('Введите число 2: ')))
    print(f"{result}")
    if input('Продолжить выполнение (да/нет): ') == 'нет':
        break


# 2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.
def get_personal_info(**kwargs):
    return list(kwargs.values())


print(
    get_personal_info(
        first_name=input('Введите Имя: '),
        second_name=input('Введите Фамилию: '),
        birthday_year=int(input('Введите год рождения: ')),
        city_name=input('Введите город проживания: '),
        email=input('Введите email: '),
        phone=input('Введите телефон: ')
    )
)


# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму наибольших двух аргументов.
def get_square_two_max_values(a, b, c):
    z = [a, b, c]
    z.remove(min(a, b, c))
    return sum(z)


print(get_square_two_max_values(4, 1, 9))


# 4. Программа принимает действительное положительное число x и целое отрицательное число y. Необходимо выполнить возведение числа x в степень y.
# Задание необходимо реализовать в виде функции my_func(x, y). При решении задания необходимо обойтись без встроенной функции возведения числа в степень.

# ** Подсказка:** попробуйте решить задачу двумя способами.
# Первый — возведение в степень с помощью оператора **.
# Второй — более сложная реализация без оператора **, предусматривающая использование цикла.
def my_func_1(x, y):
    return 1 / x ** abs(y)


print(my_func_1(2, -2))


def my_funс_2(x, y):
    for i in range(abs(y) - 1):
        x *= x
    return 1 / x


print(my_funс_2(2, -2))

# 5. Программа запрашивает у пользователя строку чисел, разделенных пробелом.
# При нажатии Enter должна выводиться сумма чисел.
# Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter.
# Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
# Но если вместо числа вводится специальный символ, выполнение программы завершается.
# Если специальный символ введен после нескольких чисел, то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу.
def user_sum_numbers():
    res = 0
    while True:
        numbers = input('Введите числа через проблем. Для выхода введите: Exit ').split()
        for i in numbers:
            try:
                if i == 'Exit':
                    print(f'Сумма введеных числен {res}. Завершение.')
                    return
                else:
                    res += int(i)
            except ValueError:
                print('Не корректное значение')
        print(f'Сумма числел: {res}')

user_sum_numbers()

# 6. Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же, но с прописной первой буквой.
# Например, print(int_func(‘text’)) -> Text.
# Продолжить работу над заданием. В программу должна попадать строка из слов, разделенных пробелом. Каждое слово состоит из латинских букв в нижнем регистре.
# Сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы. Необходимо использовать написанную ранее функцию int_func().
def int_func(text):
    return text.title()

output_text = []

for word in input('Введите строку, слова в которой разделены пробелами: ').split(' '):
    output_text.append(int_func(word))

print(f'Результат: {" ".join(output_text)}')