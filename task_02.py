# Задайте список. 
# Напишите программу, которая определит, 
# присутствует ли в заданном списке 
# строк некое число.

def find_word(str1, num):
    count = 0
    for item in str1:
        if item == num:
            count+=1
        else:count=count

    if count > 0: return (f'число найдено {count} раз')
    else: return 'не найдено' 




lst:str = [1, 22, 333, 'f...c', 'slap']
print(find_word(lst, 333))

