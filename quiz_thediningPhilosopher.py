import threading

class DiningPhilosophers(object):

    def __init__(self):
        # one lock per fork
        self.forks = [threading.Lock() for _ in range(5)]

    def wantsToEat(self, philosopher, pickLeftFork, pickRightFork, eat, putLeftFork, putRightFork):
        """
        :type philosopher: int
        :type pickLeftFork: method
        :type pickRightFork: method
        :type eat: method
        :type putLeftFork: method
        :type putRightFork: method
        :rtype: void
        """
        left = philosopher
        right = (philosopher + 1) % 5

        # avoid deadlock by picking forks in a fixed order
        first, second = (left, right) if left < right else (right, left)

        with self.forks[first]:
            with self.forks[second]:
                if first == left:
                    pickLeftFork()
                    pickRightFork()
                    eat()
                    putRightFork()
                    putLeftFork()
                else:
                    pickRightFork()
                    pickLeftFork()
                    eat()
                    putLeftFork()
                    putRightFork()
