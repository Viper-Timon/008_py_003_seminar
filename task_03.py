# 3. Напишите программу, которая определит
# позицию второго вхождения строки в
# списке либо сообщит, что её нет.

# *Пример:*
# - список: ["qwerty", "asd", "zxc", "qwerty", "ertqwe"], ищем: "qwerty", ответ: 3
# - список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
# - список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
# - список: ["123", "234", 123, "567"], ищем: "123", ответ: -1
# - список: [], ищем: "123", ответ: -1




def find_2nd_pos_word(str1, word):
    count = 0
    pos = 0
    find_pos = 0

    for i in str1:
        if i == word:
            count +=1
            if count == 2:
                find_pos = pos
        pos +=1

    if count > 1:
        return find_pos
    else: 
        return '-1'



lst = ["qwerty", "fwerty", "zxc", "fqwerty", "qwerty", "ertqwe","qwerty"]
find_word = "qwerty"
print(lst)
print(find_2nd_pos_word(lst, find_word))
