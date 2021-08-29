# Встроенная функция input позволяет ожидать и возвращать данные из стандартного
# ввода в виде строк (весь введенный пользователем текст до нажатия им enter).
# Используя данную функцию, напишите программу, которая:

# 1. После запуска предлагает пользователю ввести текст, содержащий любые слова,
# слоги, числа или их комбинации, разделенные пробелом.
# 2. Считывает строку с текстом, и разбивает его на элементы списка, считая
# пробел символом разделителя.
# 3. Печатает этот же список элементов (через пробел), однако с удаленными
# дубликатами.

# Пример:
# -> asdfdsf324 ?3 efref4r4 23r(*&^*& efref4r4 a a bb ?3
# asdfdsf324 ?3 efref4r4 23r(*&^*& a bb


# print('Введите текст, содержащий любые слова, слоги, числа или их комбинации, разделенные пробелом')

text = input('Введите текст, содержащий любые слова, слоги, числа или их комбинации, разделенные пробелом:\n ').split()
unique = []

for word in text:
    if word not in unique:
        unique.append(word)
print(' '.join(unique))

# Если сохранение порядка не важно:
# text = input('Введите текст, содержащий любые слова, слоги, числа или их комбинации, разделенные пробелом:\n ').split()
# mySet = set(text) 
# print(' '.join(mySet))
