second = int(input("Время в секундах = "))
hour = second//3600
second = second % 3600
minut = second // 60
ost_sec = second % 60
print("{:02d}:{:02d}:{:02d}".format(hour, minut, ost_sec))



