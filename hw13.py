
# Напишите функцию, которая переводит значения показаний
# температуры из Цельсия в Фаренгейт и наоборот.


def convet(x, temp_type):
    if temp_type == 'C' or temp_type == 'c':
        return 1.8 * x + 32
    elif temp_type == 'F' or temp_type == 'f':
        return (x - 32) / 1.8

print(convet(17,'c'))
