# 4. Напишите программу, которая будет
# преобразовывать десятичное число в двоичное.
#     Пример:
#     - 45 -> 101101
#     - 3 -> 11
#     - 2 -> 10


def num_transf(num, sys):
    if num/sys > 0:
        num_transf(int(num/sys), sys)
        print(int(num % sys), end="")

# можно и циклом без рекурсии

def num_transf_math(num, sys):
    comp=0
    bit_depth=1
    while num!=0:
        comp +=int(num%sys)*bit_depth
        num = int(num/sys)
        bit_depth*=10

    return comp




n = int(input('Введите число '))
culc_sys = int(input('перевести в систему счислению '))

num_transf(n, culc_sys)
print()
print(num_transf_math(n, culc_sys))







