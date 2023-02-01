# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты
# вверх одной и той же стороной. Выведите минимальное количество монет, которые нужно перевернуть
#
# 5 -> 1 0 1 1 0
# 2

from random import randint
eagle_count = 0
nut_count = 0
str_result = ""
number_of_coins = int(input("Введите количество монет: "))
for i in range(0, number_of_coins):
    throw_a_coin = randint(0, 1)
    if throw_a_coin == 0:
        eagle_count += 1
    else:
        nut_count += 1
    str_result = str_result + " " + str(throw_a_coin)
print(str_result)
if eagle_count <= nut_count:
    print(f"Минимально нужно перевернуть {eagle_count} монет")
else:
    print(f"Минимально нужно перевернуть {nut_count} монет")
