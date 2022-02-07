#value = 5 + 10
#print(value)
name = input("Укажите ваше имя: ")
age = int(input("Укажите ваш возраст: "))

print("Привет, {}! Тебе уже  {} лет!".format(name, age))

#task 2
second = int(input("Время в секундах = "))
hour = second//3600
second = second % 3600
minut = second // 60
ost_sec = second % 60
print("{:02d}:{:02d}:{:02d}".format(hour, minut, ost_sec))

#Task 3

n = input("Введите число: ")
nn = (n, n)
nnn = (n, n, n)
jnn = "".join(nn)
jnnn = "".join(nnn)
sum_nnn = int(n) + int(jnn) + int(jnnn)
print(sum_nnn)

#Task 4
n = input("Введите число: ")
mass = ",".join(n)
print("Самое большое число: ", max(mass))

#task 4.2

n = input("Введите число: ")
max_n = 0
i = 0
while i < len(n):
    if int(n[i]) > max_n:
        max_n = int(n[i])
    i += 1
print(max_n)


#task 5
revenue = int(input("Введите сумму выручки: "))
costs = int(input("Введите сумму издержек: "))
profit = revenue-costs
if revenue > costs:
    print(f"Прибыль= {profit}")
    profitability = ((profit)/revenue) * 100
    print("Рентабельность продаж: ", profitability, "%")
    employees = int(input("Введите количество сотрудников: "))
    profitability_for_one = profit/employees
    print("Прибыль фирмы в расчете на одного сотрудника: ", profitability_for_one)
else:
    print(f"Убыток= {profit}")

#task 6

a = float(input("Значение первого дня: "))
b = float(input("Значение которого нужно достич: "))
day = 1
while a < b:
    print("{}-й день: {:.2f}".format(day, a))
    day += 1
    a = a+a*0.1
print("{}-й день: {:.2f}".format(day, a))
print(f"Ответ: на {day}-й день")
