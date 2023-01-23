"""
Task_3
1. Напишіть корутину яка через метод send() отримує певне число, а повертає середнє арифметичне чисел що
були отримані раніше (включаючи те що отримали)
"""


def coroutine(func):
    def wrap(*args, **kwargs):
        g = func(*args, **kwargs)
        next(g)
        return g
    return wrap


@coroutine
def average_sum():
    i = 0
    count = 1
    while True:
        if i == 0:
            a = yield i
            i += a
        a = yield i / count
        i += a
        count += 1


gen = average_sum()
print(gen.send(1))
print(gen.send(2))
print(gen.send(3))
print(gen.send(4))
