# 1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.

with open('test01.txt', 'w+') as my_f:
    text = input('Enter text: ')
    while text:
        my_f.writelines(f"{text}\n")
        text = input('Enter text: ')
        if not text:
            break
    my_f.seek(0)
    content = my_f.read()
    print(content)

# 2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке

my_list = ['hola\n', 'señorita\n', 'adios\n']
with open("test02.txt", 'w+') as file_obj:
    file_obj.writelines(my_list)
with open("test02.txt") as file_obj:
    lines = 0
    letters = 0
    for line in file_obj:
        lines += line.count("\n")
        letters = len(line)-1
        print(f"{letters} letters in line")
    print(f"String count is {lines}")

# 3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.

firm = {'Lopez': 12000, 'Suarez': 20010, 'Bashirova': 21900, 'Alegre': 15000}
try:
    file_obj = open("test03.txt", 'w')
    for last_name, salary in firm.items():
        file_obj.write(last_name + ':' + str(salary) + "\n")
except IOError:
    print("Datos invalidos!")
finally:
    file_obj.close()
summa = 0
count = 0
persons = []
with open("test03.txt", "r") as file_obj:
    for line in file_obj:
        print(line, end="")
        tokens = line.split(':')
        if int(tokens[1]) <= 200:
            persons.append(tokens[0])
        summa += int(tokens[1])
        count += 1
result = summa / count
print(f"Salario promedio: {result}")

# 4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

translator = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
my_list = []
result = []
try:
    file_obj = open("test04.txt", 'r')
    for line in file_obj:
        tokens = line.split(" - ")
        print(tokens)
        if tokens[0] in translator:
            word = translator[tokens[0]]
            result.append(word +' - '+ tokens[1])
    print(result)
except IOError:
    print("Invalid data!")
finally:
    file_obj.close()

try:
    file_input = open("test04_new.txt", "w")
    file_input.writelines(result)
except IOError:
    print("Invalid data!")
finally:
    file_input.close()

# 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
#  Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

def summary():
    try:
        with open('test05.txt', 'w+') as file_obj:
            line = input('Enter numbers separated by a space \n')
            file_obj.writelines(line)
            my_numb = line.split()

            print(sum(map(int, my_numb)))
    except IOError:
        print('File error')
    except ValueError:
        print('Incorrect number. Input-output error')
summary()

# 6. Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие
#  лекционных, практических и лабораторных занятий по этому предмету и их количество.
#  Важно, чтобы для каждого предмета не обязательно были все типы занятий.
#  Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести словарь на экран.

def count_subjects():
    try:
        # Programming: 100(h) 50(p) 20(l)
        mydict = {}
        with open("test06.txt", encoding='utf-8') as fobj:
            for line in fobj:
                name, stats = line.split(':')  # name = Programming, stats = 100(h) 50(p) 20(l)
                name_sum = sum(map(int, ''.join([i for i in stats if i == ' ' or ('0' <= i <= '9')]).split()))
                mydict[name] = name_sum
            print(f"{mydict}")  # result:{'Programming': 170}
    except FileNotFoundError:
        return 'File not found.'


count_subjects()

# 7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме: название,
# форма собственности, выручка, издержки. Пример строки файла: firm_1 ООО 10000 5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
# Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.

import json


def get_statistics():
    try:
        with open('test07.txt', 'r+', encoding='utf-8') as file:
            statistics = []
            profit = {}
            average_profit = {}
            av = 0
            prof = 0
            i = 3
            for line in file:
                name, firm, earning, damage = line.split()
                total = int(earning) - int(damage)
                if total >= 0:
                    prof = prof + total
                else:
                    i -= 1
                profit[name] = total
            statistics.append(profit)
            if i != 0:
                (av) = prof / i
                average_profit['average_profit'] = round(av)
                statistics.append(average_profit)
            else:
                print('Все компании работают в убыток')
            print(statistics)
        with open('file.json', 'a+', encoding='utf-8') as json_file:
            json.dump(statistics, json_file)
    except FileNotFoundError:
        return 'Файл не найден.'


get_statistics()