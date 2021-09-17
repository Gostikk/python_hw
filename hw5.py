# Встроенная функция input позволяет ожидать и возвращать данные из стандартного
# ввода ввиде строки (весь введенный пользователем текст до нажатия им enter).
# Используя данную функцию, напишите программу, которая:

# 1. После запуска предлагает пользователю ввести неотрицательные целые числа,
# разделенные через пробел и ожидает ввода от пользователя.1
# 2. Находит наименьшее положительное число, не входящее в данный пользователем
# список чисел и печатает его.


# Например:

# -> 2 1 8 4 2 3 5 7 10 18 82 2
# 6


string = input('неотрицательные целые числа, разделенные через пробел: \n').split()
numbers = set(map(int, string))
for i in range(1, max(numbers)):
    if i not in numbers:
        print(i)
    else:
        print(max(numbers)+1)
