# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.
#
# 10 -> 1 2 4 8

limit = int(input("Введите число: "))
str_result = ""
for i in range(0, int(limit/2)):
    if 2**i <= limit:
        str_result = str_result + str(2**i) + " "
if str_result == "":
    print ("N меньше 2")
else:
    print(str_result)