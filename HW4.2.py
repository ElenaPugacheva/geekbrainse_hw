n = input("Введите число: ")
max_n = 0
i = 0
while i < len(n)-1:
    if int(n[i]) > max_n:
        max_n = int(n[i])
    i += 1
print(max_n)



