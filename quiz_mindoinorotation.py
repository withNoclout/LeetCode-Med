class Solution(object):
    def minDominoRotations(self, tops, bottoms):
        """
        :type tops: List[int]
        :type bottoms: List[int]
        :rtype: int
        """
        def check(x):
            rotations_a = rotations_b = 0
            for a, b in zip(tops, bottoms):
                if a != x and b != x:
                    return float('inf')
                elif a != x:
                    rotations_a += 1
                elif b != x:
                    rotations_b += 1
            return min(rotations_a, rotations_b)
        
        candidates = [tops[0], bottoms[0]]
        res = min(check(candidates[0]), check(candidates[1]))
        return res if res != float('inf') else -1
