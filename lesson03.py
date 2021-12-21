# 1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

def calculator(a, b):
    try:
        return a/b
    except ZeroDivisionError as e:
        print(f'Error! No se puede dividir por cero')


print(calculator(int(input('Primer numero: ')), int(input('Segundo numero: '))))

# 2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.


def personal_data(name, lastname, year_of_birth, city, email, phone):
    return print(f'Your name: {name} Your surname: {lastname} Year of birth {year_of_birth}' rt
                 f'Your city: {city} Email: {email} Enter your phone number: {phone}')


personal_data(
    name=input('Your name: '),
    lastname=input('Your surname: '),
    year_of_birth=input('Year of birth: '),
    city=input('Your city: '),
    email=input('Email: '),
    phone=input('Your phone number: '),
)

# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.

def my_func(arg1, arg2, arg3):
    print(f'The sum of the two largest arguments is: {arg1 + arg2 + arg3 - min([arg1, arg2, arg3])}')


my_func(
    int(input('Argument 1:')),
    int(input('Argument 2:')),
    int(input('Argument 3:')),
)

# 4. Программа принимает действительное положительное число x и целое отрицательное число y.
# Необходимо выполнить возведение числа x в степень y.
# Задание необходимо реализовать в виде функции my_func(x, y). При решении задания необходимо
# обойтись без встроенной функции возведения числа в степень.
# попробуйте решить задачу двумя способами. Первый — возведение в степень с помощью оператора **.
# Второй — более сложная реализация без оператора **, предусматривающая использование цикла.

#var 1
    def my_func(x, y):
    return x ** y

print(f'Exponentiation: '
      f'{my_func(int(input("Basis Х: ")), int(input("Degree Y: ")))}')

#var 2
x = int(input("Basis Х: "))
y = int(input("Degree Y: "))
i = 1
result = 1
while i <= x:
    result *= y
    i += 1
print(result)

# 5. Программа запрашивает у пользователя строку чисел, разделенных пробелом.
# При нажатии Enter должна выводиться сумма чисел. Пользователь может продолжить ввод чисел,
# разделенных пробелом и снова нажать Enter. Сумма вновь введенных чисел будет добавляться
# к уже подсчитанной сумме. Но если вместо числа вводится специальный символ, выполнение программы завершается.
# Если специальный символ введен после нескольких чисел, то вначале нужно добавить сумму этих чисел
# к полученной ранее сумме и после этого завершить программу.

def calculate_sum(*nums):
    sum = 0
    flag = False
    for num in nums:
        try:
            if num:
                sum += float(num)
        except ValueError:
            flag = True
    return sum, flag

general_sum = 0

while True:
    numbers_string = input('Enter numbers separated by a space: ').split(' ')
    sum, stop_flag = calculate_sum(*numbers_string)
    general_sum += sum
    print(f'Total {general_sum}')

    if stop_flag:
        break

# 6. Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же,
# но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.
def int_func ():
    wrd = input("Enter any word: ")
    print(wrd.title())
    return
int_func()

# Продолжить работу над заданием. В программу должна попадать строка из слов, разделенных пробелом.
# Каждое слово состоит из латинских букв в нижнем регистре.
# Сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы.
# Необходимо использовать написанную ранее функцию int_func()
def int_func ():
    wrd = input("Enter any phrase: ")
    print(wrd.title())
    return
int_func()