###################################################################################################

# Тинькофф задачи пробный тест

# 1
a, b, c, d = map(int, input().split())
if b > d:
    print(a)
else:
    print(a + (d - b) * c)

# 2

n = int(input())
print(n.bit_length() - (n & (n - 1) == 0))

# 3.1

n, t = map(int, input().split())
l = list(map(int, input().split()))
leave = int(input())
count = 0
count1 = l[leave - 1] - 1
if t > l[leave - 1]:
    for i in range(n):
        if i > 0 and i < n:
            count += l[i] - l[i - 1]
    print(count)
else:
    l.pop(leave - 1)
    for i in range(n - 1):
        if i > 0 and i < n:
            count += l[i] - l[i - 1]
    print(count + count1)

###################################################################################################

# Тинькофф QA mobile

#1

N = int(input())
M = int(input())
X = int(input())
Y = int(input())
# n, m = min(n, m), max(n, m)
if N > M:
    N, M = M, N
if X >= N / 2:
    X = N - X
if Y >= M / 2:
    Y = M - Y
# print(min(x, y))
if X < Y:
    print(X)
else:
    print(Y)

#2

N = int(input())
list = []
for i in range(N):
    list.append(int(input()))
print(list.count(max(list)))

#3

a = input().lower()
b = input().lower()
l1 = [ord(a[i]) for i in range(len(a))]
l2 = [ord(b[i]) for i in range(len(b))]
c = sorted(l1)
d = sorted(l2)
print(c)
print(d)
if c == d:
    print('YES')
else:
    print('NO')

#4

a = input()
b = input()
print(a.count(b))

#5

P = int(input())  # percent
X = int(input())  # RUB
Y = int(input())  # COP
K = int(input())  # YEAR

a = X + Y / 100

for i in range(1, K + 1):
    a = a * (100 + P) / 100
    a = a * 100 // 1 / 100
print(int(a), int(a % 1 * 100))

###################################################################################################

#Задачи Тинькофф разработчик
#2
a, b, c = input(), input(), input()
if a == '>' and b == '>' and c == '>':
    print('cba')
elif a == '=' and b == '>' and c == '>':
    print('cab')
    print('cba')
elif a == '>' and b == '>' and c == '=':
    print('bca')
    print('cba')
elif a == '<' and b == '<' and c == '<':
    print('abc')
elif a == '=' and b == '<' and c == '<':
    print('abc')
    print('bac')
elif a == '<' and b == '<' and c == '=':
    print('abc')
    print('acb')
elif a == '<' and b == '>' and c == '>':
    print('cab')
elif a == '>' and b == '>' and c == '<':
    print('bca')
elif a == '>' and b == '<' and c == '<':
    print('bac')
elif a == '<' and b == '<' and c == '>':
    print('acb')
elif a == '>' and b == '=' and c == '<':
    print('bac')
    print('bca')
elif a == '<' and b == '=' and c == '>':
    print('acb')
    print('cba')

#3

print(input().strip('0').count('0'))

l = []
for i in range(1, 2023):
    l.append(i ** 2)

###################################################################################################

#Задачи Тинькофф инженер
l1 = l[::4]
l2 = l[1::4]
l3 = l[2::4]
l4 = l[3::4]
print(sum(l1) + sum(l2) - sum(l3) - sum(l4))
