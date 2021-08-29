from functools import reduce


print('problem #6:', sum([i for i in range(1,101)])**2 - sum([i**2 for i in range(1,101)]))
print('problem #9:', [a * b * c for a in range(501) for b in range(a+1,501) for c in range(b+1, 501) if a**2 + b**2 == c**2 and a + b + c == 1000][0])
print('problem #40: ', reduce(lambda x, y: x * y, [int(''.join([str(i) for i in range(200000)])[10**k]) for k in range(7)]))
print('problem #48: ', (str(sum([i**i for i in range(1,1001)])))[-10:])