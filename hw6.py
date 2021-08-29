# https://projecteuler.net/problem=36

# The decimal number, 585 = 1001001001 in binary, is palindromic in both bases.
# Find the sum of all numbers, less than one million, which are palindromic in
# base 10 and base 2. (Please note that the palindromic number,
# in either base, may not include leading zeros.)

# Напишите программу, которая решает описанную выше задачу и печатает ответ.


def Is_palidromic(x):
    if str(x) == str(x)[::-1] and bin(x)[2:] == bin(x)[:1:-1]:
        return True

res = 0
for i in range(1,1000000,2):
    if Is_palidromic(i):
        res += i

print(res)
