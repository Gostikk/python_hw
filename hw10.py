# Гипотеза Коллатца
# может быть кратко выражена следующим образом:

# берём любое натуральное число n, если оно чётное,
# то делим его на 2 если нечётное, то умножаем на 3
# и прибавляем 1 (получаем 3n + 1) над полученным
# числом выполняем те же самые действия, и так далее.

# Гипотеза Коллатца заключается в том, что какое бы
# начальное число n мы ни взяли, рано или поздно мы
# получим единицу.

# Задача
# Вычислить число шагов для числа n, согласно гипотезе
# Коллатца необходимых для достижения этим числом единицы.

# |      n      | кол-во шагов |
# |----------------------------|
# |     177     |      31      |
# |    2139     |      76      |
# |   2999991   |      182     |
# |   2999991   |      108     |
# | 12345678911 |      243     |



def Collac(x, steps=0):
    if x == 1:
        return steps
    steps += 1
    if x % 2 == 0:
        return Collac(x / 2, steps)
    else:
        return Collac(x*3 + 1, steps)


print(Collac(12345678911))