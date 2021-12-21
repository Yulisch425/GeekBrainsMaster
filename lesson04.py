# 1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной
# платы сотрудника. В расчете необходимо использовать формулу: (выработка в часах*ставка в
# час) + премия. Для выполнения расчета для конкретных значений необходимо запускать
# скрипт с параметрами.

def simple_calc():
    x = float(input('Hours of work : '))
    y = float(input('Cost of one hour : '))
    c = float(input('Bonus - '))
    pay = x * y
    return pay + c
print(f'Salary amount is : {simple_calc() }')

# 2. Представлен список чисел. Необходимо вывести элементы исходного списка,
# значения которых больше предыдущего элемента.

result_list = []
list = [int(i) for i in input("Enter numbers separated by a space: ").split()]
for i in range(1, len(list)):
    if list[i] > list[i-1]:
        (result_list.append(list[i]))
print("Original list: ", list)
print("Rating result list: ", result_list)

# 3. Для чисел в пределах от 20 до 240 найти числа, кратные 20 или 21. Необходимо решить задание в одну строку.

list = [i for i in range(20, 240) if i % 20 == 0 or i % 21 == 0]

print("Список чисел кратных 20 или 21 в диапазоне [20..240): ", list)

# 4. Представлен список чисел. Определить элементы списка, не имеющие повторений.
# Сформировать итоговый массив чисел, соответствующих требованию. Элементы вывести в порядке
# их следования в исходном списке. Для выполнения задания обязательно использовать генератор.

my_list = [3, 8, 9, 4, 2, 1, 7, 1, 5, 3]
print("Original elements:\n", my_list)
new_list = [i for i in my_list if my_list.count(i) == 1]
print("List elements without repetition:\n", new_list)

# 5. Реализовать формирование списка, используя функцию range() и возможности генератора.
# В список должны войти четные числа от 100 до 1000 (включая границы).
# Необходимо получить результат вычисления произведения всех элементов списка.

from functools import reduce

list = [i for i in range(100, 1001, 2)]
print("All even numbers in the range [100..1000]:\n", list)
print("Multiplication of all list items:\n", reduce(lambda x,y: x*y, list))

# 6. Реализовать два небольших скрипта:
# а) итератор, генерирующий целые числа, начиная с указанного,

from itertools import count

print("<<Infinite interator, specified starting>>")
n = int(input("Enter any whole number:"))

for i in count(n):
    print(i, end=' ')

# б) итератор, повторяющий элементы некоторого списка, определенного заранее.

from itertools import cycle

list = [4, 8, 3, 2, 7, 4, 2, 5, 9, 6]
for i in cycle(list):
    print(i, end=' ')

# 7. Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение.
# При вызове функции должен создаваться объект-генератор. Функция должна вызываться следующим образом:
# for el in fact(n).
# Функция отвечает за получение факториала числа, а в цикле необходимо выводить только первые n чисел,
# начиная с 1! и до n!.

from math import factorial

def factorial_gen(n):
    for i in range(n):
        print(i, end='! = ')
        yield factorial(i)

print("<<Factorial number calculating>>")
for el in factorial_gen(15):
    print(el)