# 5. * Задайте число. Составьте список чисел Фибоначчи,
# в том числе для отрицательных индексов.
#     Пример:
#     - для k = 8 список будет выглядеть так:
# [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] [Негафибоначчи]


def negafibonacci(n):
    a = []
    for i in range(n):
        if i == 0:
            a.append(0)
        elif i == 1:
            a.append(1)
        else:
            a.append(a[i-1]+a[i-2])
    

    b=[]
    negative=1
    for i in range(n):
        negative*=-1
        if i==0:
            b.append(0)
        else:
            b.append(a[i])
            b.insert(0,a[i]*negative)

    return b


num=int(input('Введите число Негафибоначи -> '))
print(negafibonacci(num))