class Solution(object):
    def doesValidArrayExist(self, derived):
        return sum(derived) % 2 == 0
