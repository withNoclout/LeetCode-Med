import threading

class H2O(object):
    def __init__(self):
        self.h_sem = threading.Semaphore(2)
        self.o_sem = threading.Semaphore(0)
        self.lock = threading.Lock()
        self.h_count = 0

    def hydrogen(self, releaseHydrogen):
        """
        :type releaseHydrogen: method
        :rtype: void
        """
        self.h_sem.acquire()
        releaseHydrogen()
        with self.lock:
            self.h_count += 1
            if self.h_count == 2:
                self.o_sem.release()
                self.h_count = 0

    def oxygen(self, releaseOxygen):
        """
        :type releaseOxygen: method
        :rtype: void
        """
        self.o_sem.acquire()
        releaseOxygen()
        self.h_sem.release()
        self.h_sem.release()
