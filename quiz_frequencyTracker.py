class FrequencyTracker(object):

    def __init__(self):
        self.count = collections.defaultdict(int)
        self.freq = collections.defaultdict(int)

    def add(self, number):
        if self.count[number] > 0:
            self.freq[self.count[number]] -= 1
        self.count[number] += 1
        self.freq[self.count[number]] += 1

    def deleteOne(self, number):
        if self.count[number] > 0:
            self.freq[self.count[number]] -= 1
            self.count[number] -= 1
            if self.count[number] > 0:
                self.freq[self.count[number]] += 1

    def hasFrequency(self, frequency):
        return self.freq[frequency] > 0
