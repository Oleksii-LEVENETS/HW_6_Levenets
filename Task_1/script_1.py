"""
Task_1.
1. Напишіть ітератор який приймає додатнє число n і видає всі числа фібоначі від 0 до n
(якщо число більше чим n, то воно не повертається). Добавте метод який перевіряє чи поточний стан ітератора
– парне число.

Добавте метод який перевіряє чи поточний стан ітератора --
мається на увазі що в ітераторі буде метод, наприклад, is_odd() -> bool
і ви тоді можете в любий момент робити fib.is_odd()
"""


class FibonacciNumbers:
    def __init__(self, stop):
        self.current = 0
        self.next = 1
        self.stop = stop

    def __iter__(self):
        return self

    def __next__(self):
        if self.next > self.stop:
            raise StopIteration

        next_num = self.current + self.next
        self.current = self.next
        self.next = next_num
        return self.current

    def is_even(self):
        print("The current number of Iterator is even (True/False): ", end="")
        if self.current % 2 == 0:
            return True
        else:
            return False


fib = FibonacciNumbers(50)
for i in fib:
    print(i)

print(fib.is_even())
