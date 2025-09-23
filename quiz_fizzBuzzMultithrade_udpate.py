import threading

class FizzBuzz(object):
    def __init__(self, n):
        self.n = n
        self.i = 1
        self.lock = threading.Lock()
        self.c = threading.Condition(self.lock)

    # printFizz() outputs "fizz"
    def fizz(self, printFizz):
        while True:
            with self.c:
                while self.i <= self.n and not (self.i % 3 == 0 and self.i % 5 != 0):
                    self.c.wait()
                if self.i > self.n:
                    self.c.notify_all()
                    return
                printFizz()
                self.i += 1
                self.c.notify_all()

    # printBuzz() outputs "buzz"
    def buzz(self, printBuzz):
        while True:
            with self.c:
                while self.i <= self.n and not (self.i % 3 != 0 and self.i % 5 == 0):
                    self.c.wait()
                if self.i > self.n:
                    self.c.notify_all()
                    return
                printBuzz()
                self.i += 1
                self.c.notify_all()

    # printFizzBuzz() outputs "fizzbuzz"
    def fizzbuzz(self, printFizzBuzz):
        while True:
            with self.c:
                while self.i <= self.n and not (self.i % 3 == 0 and self.i % 5 == 0):
                    self.c.wait()
                if self.i > self.n:
                    self.c.notify_all()
                    return
                printFizzBuzz()
                self.i += 1
                self.c.notify_all()

    # printNumber(x) outputs "x"
    def number(self, printNumber):
        while True:
            with self.c:
                while self.i <= self.n and not (self.i % 3 != 0 and self.i % 5 != 0):
                    self.c.wait()
                if self.i > self.n:
                    self.c.notify_all()
                    return
                printNumber(self.i)
                self.i += 1
                self.c.notify_all()
