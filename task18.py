# Задача 18: Требуется найти в массиве из случайных чисел(от 1 до n)
#            самый близкий по величине элемент к заданному числу X.
#            Пользователь в первой строке вводит натуральное
#            число N – количество элементов в массиве.
#            Последняя строка содержит число X

# *Пример:*

# 5
# 1 2 3 4 5
# 6
# -> 5

N = int(input("Введите кол-во элементов списка: "))

list_a = []

for i in range(N):
    list_a.append(int(input("Введите элемент списка: ")))

X = int(input("Введите число, к которому нужно найти близкий по значению элемент в списке: "))


min_diff = max(list_a)
index_item = 0

for i in range(len(list_a)):
    if X >= list_a[i]:
        if X - list_a[i] <= min_diff:
            min_diff = X - list_a[i]
            index_item = i
    elif X < list_a[i]:
        if list_a[i] - X < min_diff:
            min_diff = list_a[i] - X
            index_item = i

print(f"-> {list_a[index_item]}")
