# Задача 16: Требуется вычислить,
#            сколько раз встречается некоторое число X в массиве из случайных чисел.
#            Пользователь в первой строке вводит натуральное
#            число N – количество элементов в массиве. Последняя строка содержит число X
# *Пример:*
# 5
# 1 2 3 4 5
# 3
# -> 1

N = int(input("Введите количество элементов списка: "))

list_a = []

for i in range(N):
    list_a.append(int(input("Введите элемент списка: ")))

X = int(input("Введите искомое число: "))

count = 0
for i in list_a:
    if X == i:
        count += 1

print(f"-> {count}")
