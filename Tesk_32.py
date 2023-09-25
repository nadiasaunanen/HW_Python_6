# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)

from random import randrange
n = int(input("Введите количество элементов cписка: "))
list_1 = [randrange(1, 100) for i in range(n)]
list_2 = []
print(list_1)
max = int(input("Введите максимальное значение: "))
min = int(input("Введите минимальное значение: "))
for i in range(len(list_1)):
    if list_1[i] >= min and list_1[i] <= max:
        list_2.append(i)
print(list_2)
