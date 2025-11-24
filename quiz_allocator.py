class Allocator(object):

    def __init__(self, n):
        self.memory = [0] * n

    def allocate(self, size, mID):
        free = 0
        for i in range(len(self.memory)):
            if self.memory[i] == 0:
                free += 1
                if free == size:
                    start = i - size + 1
                    self.memory[start : i+1] = [mID] * size
                    return start
            else:
                free = 0
        return -1

    def freeMemory(self, mID):
        cnt = 0
        for i in range(len(self.memory)):
            if self.memory[i] == mID:
                self.memory[i] = 0
                cnt += 1
        return cnt
