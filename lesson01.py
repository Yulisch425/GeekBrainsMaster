# Задача-1: Поработайте с переменными, создайте несколько, выведите на экран,
# запросите у пользователя несколько чисел и строк и сохраните в переменные, выведите на экран.

x = input("Enter your name: ")
print(x)
age = int(input("Enter your age: "))
print(age)
z = float(input("Choose any number: "))
print("Nice to meet you " + x)

# Задача-2: Пользователь вводит время в секундах.
# Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
# Используйте форматирование строк.

seconds = int(input("Write your time in seconds "))
print("Well, let's convert this to regular view ")
sec = seconds % (24 * 3600)
hour = sec // 3600
sec %= 3600
min = sec // 60
sec %= 60
print(f"It's {hour}:{min}:{sec} ")

# Задача-3: Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.

x = input("Wanna see a magic? Choose number: ")
print(f"You choose " + x)
print("Let's magic happens! ")
a = int(x + x)
b = int(x+x+x)
total = int(x) + a + b
print("Your magic number is %s!" % total)

# Задача-4: Пользователь вводит целое положительное число.
# Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.

number = input("Write a number: ")
print(number)
x = 0
for i in number:
    while int(i) > x:
        x = int(i)
print("The biggest digit in your number is %s!" % x)

# Задание-5:
# Запросите у пользователя значения выручки и издержек фирмы.
# Определите, с каким финансовым результатом работает фирма
# (прибыль — выручка больше издержек, или убыток — издержки больше выручки).
# Выведите соответствующее сообщение.
# Если фирма отработала с прибылью, вычислите рентабельность выручки (соотношение прибыли к выручке).
# Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.

proceed = int(input("Enter company's proceed: "))
print(proceed)
outlay = int(input("Enter company's outlay: "))
print(outlay)
if proceed > outlay:
    profitability = proceed-outlay
    rent = profitability/proceed
    print(f"It's great! The company has {profitability} profitability")
    employer = int(input("How many employers are in the company: "))
    print(f"{profitability/employer} for every employer")
elif proceed == outlay:
    print("You have to try a little bit more")
else:
    print("Seems you have to work harder to improve earnings")

# Задача-6:
# Спортсмен занимается ежедневными пробежками. В первый день его результат составил a километров.
# Каждый день спортсмен увеличивал результат на 10 % относительно предыдущего.
# Требуется определить номер дня, на который общий результат спортсмена составить не менее b километров.
# Программа должна принимать значения параметров a и b и выводить одно натуральное число — номер дня.

a = float(input("It's your first day of run. How many km you have run today: "))
print(a)
b = float(input("What is your daily goal in km "))
print(b)
day = 1
if a > b:
    print(day)
while a < b:
    a = a + a/10
    day += 1
print("You will reach your goal by day %s!" % day)
