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
    print(f"Убыток= {profit}" )



