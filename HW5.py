revenue = int(input("Введите сумму выручки: "))
costs = int(input("Введите сумму издержек: "))
if revenue > costs:
    print("Прибыль")
    profitability = ((revenue-costs)/revenue) * 100
    print("Рентабельность продаж: ", profitability, "%")
    employees = int(input("Введите количество сотрудников: "))
    profitability_for_one = (revenue-costs)/employees
    print("Прибыль фирмы в расчете на одного сотрудника: ", profitability_for_one)
else:
    print("Убыток")



