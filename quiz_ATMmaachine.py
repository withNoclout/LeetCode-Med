class ATM(object):

    def __init__(self):
        # store counts for banknotes [20, 50, 100, 200, 500]
        self.notes = [0] * 5
        self.values = [20, 50, 100, 200, 500]

    def deposit(self, banknotesCount):
        for i in range(5):
            self.notes[i] += banknotesCount[i]

    def withdraw(self, amount):
        used = [0] * 5
        # try large → small
        for i in range(4, -1, -1):
            take = min(self.notes[i], amount // self.values[i])
            used[i] = take
            amount -= take * self.values[i]

        if amount > 0:
            return [-1]

        # apply withdrawal
        for i in range(5):
            self.notes[i] -= used[i]

        return used
