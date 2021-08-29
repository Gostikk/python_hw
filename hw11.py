# Напишите функцию letters_range, которая ведет себя
# похожим на range образом, однако в качестве start и
# stop принимает не числа, а буквы латинского алфавита
# (в качестве step принимает целое число) и возращает
# не перечисление чисел, а список букв, начиная с
# указанной в качестве start, до указанной в качестве
# stop с шагом step (по умолчанию равным 1).


def letters_range(start, stop, step=1):
    for i in range(ord(start.lower()),ord(stop.lower()) + 1 ,step):
        yield chr(i)

print(list(letters_range('f', 'w', 2)))
print(list(letters_range('p', 'v')))
print(list(letters_range('a', 'z', 2)))