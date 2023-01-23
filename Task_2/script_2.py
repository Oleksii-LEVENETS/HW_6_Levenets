"""
Task_2
2. Напишіть нескінченний генератор ідентифікаторів, ID створюється по шаблону “{prefix}-{number}”.
Де prefix – рядок що отримується від користувача, а number – інкремент.
Приклад використання – в генератор передається префікс ID, генератор при кожному звернені повертає
ID-1
ID-2
ID-3
якщо префікс INTERNAL-ID INTERNAL-ID-1 INTERNAL-ID-2 INTERNAL-ID-3
і т.д.
Якщо префікс не передається, то повертати потрібно тільки інкремент
1
2
3
Генератор завжди повертає тип даних string!
"""

PREFIX = input()


def id_gen(prefix=None):
    i = 1
    while True:
        if prefix:
            yield f"{prefix}-{i}"
        else:
            yield i
        i += 1


id_generator = id_gen(PREFIX)

print(next(id_generator))
print(next(id_generator))
print(next(id_generator))
print(next(id_generator))
print(next(id_generator))
