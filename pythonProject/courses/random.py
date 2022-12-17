import random
l = {1:'Орел', 2:'Решка'}
n = int(input())    # количество попыток
for i in range(n):
    print(l[random.randint(1, 2)])

###################################################################################################

import string
print(string.ascii_letters)
print(string.ascii_uppercase)
print(string.ascii_lowercase)
print(string.digits)
print(string.hexdigits)
print(string.octdigits)
print(string.punctuation)
print(string.printable)

###################################################################################################

# Определение числа Pi методом Монте-Карло
import random
k = 0
s0 = 4
n = 10**6       # количество испытаний
for _ in range(n):
    x = random.uniform(-1,1)
    y = random.uniform(-1,1)
    if x**2 + y**2 <= 1 and x**2 + y**2 >= -1:
        k += 1
print((k/n)*s0)