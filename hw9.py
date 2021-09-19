from functools import reduce


print('problem #6:', sum([i for i in range(1,101)])**2 - sum([i**2 for i in range(1,101)]))
print('problem #9:', [b * a * ((1000 - a) - b) for b in range(1, 1001) for a in range(1, b) if a ** 2 + b ** 2 == ((1000 - a) - b) ** 2][0])
print('problem #40: ', reduce(lambda x, y: x * y, [int(''.join([str(i) for i in range(200000)])[10**k]) for k in range(7)]))
print('problem #48: ', (str(sum([i**i for i in range(1,1001)])))[-10:])