"""
Task_2
1. Напишіть генератор який приймає число d (фіксована різниця між членами арифметичної прогресії) і
кожним викликом next даний генератор повертає наступний член арифметичної прогресії.
"""


def a_progression(start, d):
    while True:
        num = start + d
        yield num
        start = num


gen = a_progression(1, 10)
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
