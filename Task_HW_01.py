# 1. Задайте список из нескольких чисел.
# Напишите программу, которая найдёт сумму
# элементов списка, стоящих на нечётной позиции.
#     Пример:
#     - [2, 3, 5, 9, 3]
# -> на нечётных позициях элементы 3 и 9, ответ: 12


lst = [2, 3, 5, 9, 3]
sum = 0
size = len(lst)
for i in range(1, size, 2):
    sum += int(lst[i])
print(sum)


# №2
sum2 = 0
count = 0
for i in lst:
    if count%2!=0:
        sum2 += int(i)
    count+=1    
print(sum)