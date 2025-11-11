class Solution(object):
    def minimumRefill(self, plants, capacityA, capacityB):
        i, j = 0, len(plants) - 1
        a, b = capacityA, capacityB
        refills = 0

        while i < j:
            if a < plants[i]:
                refills += 1
                a = capacityA
            a -= plants[i]
            i += 1

            if b < plants[j]:
                refills += 1
                b = capacityB
            b -= plants[j]
            j -= 1

        if i == j and max(a, b) < plants[i]:
            refills += 1

        return refills
