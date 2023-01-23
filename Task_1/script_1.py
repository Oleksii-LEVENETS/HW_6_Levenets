"""
Task_1.
1. Напишіть ітератор який приймає додатнє число n і видає всі числа фібоначі від 0 до n
(якщо число більше чим n, то воно не повертається). Добавте метод який перевіряє чи поточний стан ітератора
– парне число.
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
            if self.current % 2 == 0:
                print(f"{self.current} is even")
            else:
                print(f"{self.current} is odd")
            raise StopIteration

        next_num = self.current + self.next
        self.current = self.next
        self.next = next_num
        return self.current


fib = FibonacciNumbers(40)
for i in fib:
    print(i)
