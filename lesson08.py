''' 1. 1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата
«день-месяц-год». В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число,
месяц, год и преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod,
должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).

Проверить работу полученной структуры на реальных данных.
'''


class Date:
    date: str
    def __init__(self, date):
        self.date = date

    @classmethod
    def dd1(cls, self):
        d = int(self.date[0:2])
        m = int(self.date[3:5])
        y = int(self.date[6:10])
        return Date.valid(d, m, y)

    @staticmethod
    def valid(d, m, y):
        if 0 < d < 32:
            if 0 < m < 13:
                if 0 < y < 2022:
                    return f'Day: {d}\nMonth: {m}\nYear: {y}'


d1 = Date("20-12-2022")
print(Date.dd1(d1))

''' 2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль. 
Проверьте его работу на данных, вводимых пользователем. При вводе пользователем нуля в качестве делителя 
программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.
'''


class ZeroError(Exception):
    def __str__(self):
        return f'No se puede dividir por cero!'
class Del:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def dell(self):
        if self.y == 0:
            raise ZeroError
        else:
            return self.x/self.y
d = Del(666, 0)
try:
    print(d.dell())
except ZeroError as exeption:
    print("No se puede dividir por cero!")

''' 3. Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел. 
Проверить работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и заполнять список. 
Класс-исключение должен контролировать типы данных элементов списка.
'''


class Error:
    def __init__(self, *args):
        self.my_list = []

    def mylist(self):
        while True:
            try:
                val = int(input('Enter your single whole number: '))
                self.my_list.append(val)
                print(f'Actual list: {self.my_list} \n ')
            except:
                print(f"Is not a number!")
                stop = input(f'Want to try again? "Stop" to exit or any symbol to continue.')

                if stop == 'stop':
                    return f'You are out'
                else:
                    print(try_except.mylist())


try_except = Error(1)
print(try_except.mylist())

''' 4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. 
А также класс «Оргтехника», который будет базовым для классов-наследников. 
Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс). В базовом классе определить параметры, 
общие для приведенных типов. В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.
'''


class OfficeEquipment:
    model: str
    price: int
    def __init__(self, model, price):
        self.model = model
        self.price = price


class Printer(OfficeEquipment):
    model = 'PrinterCanon'
    common_price = 8000
    printing_technology = 'laser'


class Scanner(OfficeEquipment):
    model = 'ScannerSamsung'
    common_price = 10000
    scanner_type = 'sheet-feed'


class Copier(OfficeEquipment):
    model = 'CopierXerox'
    common_price = 15000
    copier_type = 'digital-type'

''' 5. Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на склад 
и передачу в определенное подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники, 
а также других данных, можно использовать любую подходящую структуру, например словарь.
'''
