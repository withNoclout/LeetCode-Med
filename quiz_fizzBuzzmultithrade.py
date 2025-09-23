from threading import Semaphore

class FizzBuzz(object):
    def __init__(self, n):
        self.n = n
        self.current = 1
        self.lock = Semaphore(1)

    # printFizz() outputs "fizz"
    def fizz(self, printFizz):
        for i in range(1, self.n + 1):
            if i % 3 == 0 and i % 5 != 0:
                with self.lock:
                    printFizz()

    # printBuzz() outputs "buzz"
    def buzz(self, printBuzz):
        for i in range(1, self.n + 1):
            if i % 5 == 0 and i % 3 != 0:
                with self.lock:
                    printBuzz()

    # printFizzBuzz() outputs "fizzbuzz"
    def fizzbuzz(self, printFizzBuzz):
        for i in range(1, self.n + 1):
            if i % 15 == 0:
                with self.lock:
                    printFizzBuzz()

    # printNumber(x) outputs "x", where x is an integer.
    def number(self, printNumber):
        for i in range(1, self.n + 1):
            if i % 3 != 0 and i % 5 != 0:
                with self.lock:
                    printNumber(i)
