#1. Создать список и заполнить его элементами различных типов данных.
# Реализовать скрипт проверки типа данных каждого элемента.
# Использовать функцию type() для проверки типа.
# Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.
#
#types_data = ["текст", 1, 4.58, None, False, (1,2,2), {1,2,3}, [1,2,3], {"name": "Ivan", "age": 25 }]
#j=1
#for i in types_data:
#    print(f"Тип данных элемента {j}:", type(i))
#    j+=1

# 2. Для списка реализовать обмен значений соседних элементов, т.е.
# Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().

result_list = [input("Вводите значения без пробелов: ")]
result_list1 = ",".join(result_list)
change = []
long = len(result_list1)
for j in range(long):
    if j % 2 == 0:
        continue
    else:
        a = result_list1[j]
        change.append(a)
        change.append(result_list1[j-1])
if long % 2 != 0:
    change.append(result_list1[long-1])
print(change)

# 3. Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.
# Ршение 1

month_number = int(input("Введите номер месяца от 1 до 12: "))
spring = [3, 4, 5]
summer = [6, 7, 8]
autumn = [9, 10, 11]
winter = [12, 1, 2]
if month_number in spring:
    print("Время года: Весна")
elif month_number in summer:
    print("Время года: Лето")
elif month_number in autumn:
    print("Время года: Осень")
elif month_number in winter:
    print("Время года: Зима")
else:
    print("Ввели не верное значение")


# Решение 2

season = {1: "Зима", 2: "Зима", 3: "Весна", 4: "Весна", 5: "Весна", 6: "Лето", 7: "Лето", 8: "Лето",
          9: "Осень", 10: "Осень", 11: "Осень", 12: "Зима"
          }
print(f"Время года: {season[int(input('Введите номер месяца от 1 до 12: '))]}")


# 4. Пользователь вводит строку из нескольких слов, разделённых пробелами.
# Вывести каждое слово с новой строки. Строки необходимо пронумеровать.
# Если в слово длинное, выводить только первые 10 букв в слове.
string_old = input("Введите предложение: ")
new_string = string_old.split(' ')
for i in new_string:
    print(i[:10])

# 5. Реализовать структуру «Рейтинг», представляющую собой
# не возрастающий набор натуральных чисел.
# У пользователя необходимо запрашивать новый элемент рейтинга.
# Если в рейтинге существуют элементы с одинаковыми значениями,
# то новый элемент с тем же значением должен разместиться после них.
# Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
# Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
# Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
# Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.
#
# Набор натуральных чисел можно задать непосредственно в коде, например, my_list = [7, 5, 3, 3, 2].
my_list = [7, 5, 3, 3, 2]
my_list.append(int(input("Введите новое значение для добавления в рейтинг: ")))
my_list.sort(reverse=True)
print(my_list)

# 6. *Реализовать структуру данных «Товары».
# Она должна представлять собой список кортежей.
# Каждый кортеж хранит информацию об отдельном товаре.
# В кортеже должно быть два элемента — номер товара и словарь с параметрами
# (характеристиками товара: название, цена, количество, единица измерения).
# Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.
# Пример готовой структуры:
#
# [
#     (1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
#     (2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
#     (3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
# ]
# Необходимо собрать аналитику о товарах. Реализовать словарь, в котором каждый ключ — характеристика товара, например название, а значение — список значений-характеристик, например список названий товаров.
# Пример:
#
# {
# “название”: [“компьютер”, “принтер”, “сканер”],
# “цена”: [20000, 6000, 2000],
# “количество”: [5, 2, 7],
# “ед”: [“шт.”]
# }

catalog = []
#что хочет сделать пользователь
i = 1

while True:
    control = input("Чтобы добавить товар в каталог введите Д, что бы посмотреть аналитику введите А, нажмите любую кнопку, что бы посмотреть каталог").upper()
    if control == "Д":
        namber = int(input("Введите количество товара которое хотите записать в каталог: "))
        for j in range(namber):
            product = {"Название": input("Название: "), "Цена": input("Цена: "), "Количество": input("Количество: "), "ед.": input("ед.: ") }
            catalog.append((i, product))
            i+=1
    elif control == "А":
        names = []
        count = []
        prices = []
        units = []
        for tuple in catalog:
            value = tuple[1]
            names.append(value["Название"])
            count.append(value["Количество"])
            prices.append(value["Цена"])
            units.append(value["ед."])

        print(f"Название: {names}")
        print(f"Количество: {count}")
        print(f"Цена: {prices}")
        print(f"Ед.: {units}")
    else:
        for i in catalog:
            print(i)
