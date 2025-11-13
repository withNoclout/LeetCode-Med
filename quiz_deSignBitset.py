class Bitset(object):

    def __init__(self, size):
        self.size = size
        self.bits = [0] * size
        self.flipped = False
        self.ones = 0

    def fix(self, idx):
        bit = self.bits[idx] ^ self.flipped
        if bit == 0:
            self.bits[idx] ^= 1
            self.ones += 1

    def unfix(self, idx):
        bit = self.bits[idx] ^ self.flipped
        if bit == 1:
            self.bits[idx] ^= 1
            self.ones -= 1

    def flip(self):
        self.flipped = not self.flipped
        self.ones = self.size - self.ones

    def all(self):
        return self.ones == self.size

    def one(self):
        return self.ones > 0

    def count(self):
        return self.ones

    def toString(self):
        if not self.flipped:
            return ''.join(str(b) for b in self.bits)
        else:
            return ''.join(str(1 - b) for b in self.bits)
