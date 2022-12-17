def factorial(x):  # функция факториала
    pr = 1
    for i in range(2, x + 1):
        pr = pr * i
    return pr


def sochet(n, k):  # функция определение числа сочетаний
    return factorial(n) / (factorial(k) * factorial(n - k))

print(sochet(12, 5))

###################################################################################################

def SquareandPer(a, b):     #функция нахождения площади и периметра
    return a * b, 2 * (a + b)


square, perimetr = SquareandPer(2, 5)

print(square, perimetr)

###################################################################################################

import random


def get_even(lst):
    """
    Функция создает список четных чисел
    :param lst: список
    :return:
    """
    even_lst = []
    for elem in lst:
        if elem % 2 == 0:
            even_lst.append(elem)
    return even_lst


numbers = []
for i in range(10):
    numbers.append(random.randint(0, 9))

print('numbers:', numbers)
even = get_even(numbers)
print('even', even)

###################################################################################################


from typing import List, Dict, Optional, Any, Union


# Аннотация не обязательная часть кода, а предупреждение о типе вводимых данных
def add_numbers(a: int, b: Optional[int] = None) -> int:
    return a + b


def list_upper(lst: List[str]):
    for elem in lst:
        print(elem.upper())


d: Dict[str, int] = {'a': 100, 'b': 200}

first: int = 100
second: int = 200
print(add_numbers(first, second))
print(add_numbers('hello', 'world'))
print(add_numbers([1, 2, 3, 4], [5, 6, 7, 8, 8]))
print(add_numbers.__annotations__)

###################################################################################################

#Рекурсивная функция нахождения факториала
def fact(x):
    if x == 1:
        return 1
    return fact(x - 1) * x

print(fact(4))
print(fact(10))

#Рекурсивная функции нахождения n-ого числа Фибоначчи

def fib(n):
    if n==1:
        return 0
    if n==2:
        return 1
    return fib(n-1)+fib(n-2)

print(fib(40))

#Палиндром

def palindrom(s):
    if len(s)<=1:
        return True
    if s[0] !=s[-1]:
        return False
    return palindrom(s[1:-1])
n=input()
print(palindrom(n))

###################################################################################################

# decorator

def decorator(func):
    def inner(*args, **kwargs):
        print("Start decorator...")
        func(*args, **kwargs)
        print("Finish decorator...")

    return inner


def say(name, surname):
    print('Hello', name, surname)

# decorator 1

def header(func):
    def inner(*args, **kwargs):
        print('<h1>')
        func(*args, **kwargs)
        print('</h1>')

    return inner


def table(func):
    def inner(*args, **kwargs):
        print('<table>')
        func(*args, **kwargs)
        print('</table>')

    return inner


@table
@header  # say = header((table(say))
def say(name, surname, age):
    print('Hello', name, surname)

say('Vasya', 'Ivanov', 30)

###################################################################################################

# 10.3 Функция map Python
# class map(object)
#   map(fuc, *iterables) --> map object
# map object - представляет собой итератор который вычисляет результат работы функции которую вы передали
# на каждый аргумент из этой последовательности

a = [-1, 2, -3, 4, 5]
b = list(map(abs, a))  # вворачиваем в вызов функции list
print(b)  # <map object at 0x7f431d2a5fa0>
# другой способ написания этой программы
c = [abs(i) for i in a]
print(c)  # [1, 2, 3, 4, 5]


# так же мы можем передавать функции которые сами создали

def f(x):
    return x ** 2


t = [-1, 2, -3, 4, 5]
e = list(map(f, t))  # передали нашу созданную функцию f
print(e)  # [1, 4, 9, 16, 25]
# пример со строками
s = ['hello', 'hi', 'helloworld']
n = list(map(len, s))
print(n)  # [5, 2, 10]
# в качестве функции мы можем передавать не только встроенные и самописные функции но и методы этих объектов
s = ['hello', 'hi', 'helloworld']
n = list(map(str.upper, s))
print(n)  # ['HELLO', 'HI', 'HELLOWORLD']
# так же в функцию мап можно передавать анонимную функцию
s = ['hello', 'hi', 'helloworld']
n = list(map(lambda x: x[::-1], s))
print(n)  # ['olleh', 'ih', 'dlrowolleh']
o = list(map(lambda x: x + '!', s))
print(o)  # ['hello!', 'hi!', 'helloworld!']
# так же можно строку переобразовать в список
p = list(map(list, s))
print(p)  # [['h', 'e', 'l', 'l', 'o'], ['h', 'i'], ['h', 'e', 'l', 'l', 'o', 'w', 'o', 'r', 'l', 'd']]
m = list(map(sorted, p))  # сортируем список p
print(m)

k = map(int, input().split())  # что вводить неопределённое количества чисел через пробел
print(k)