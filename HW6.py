a = float(input("Значение первого дня: "))
b = float(input("Значение которого нужно достич: "))
day = 1
while a < b:
    print("{}-й день: {:.2f}".format(day, a))
    day += 1
    a = a+a*0.1
print("{}-й день: {:.2f}".format(day, a))
print(f"Ответ: на {day}-й день спортсмен достиг результата — не менее {b} км.")