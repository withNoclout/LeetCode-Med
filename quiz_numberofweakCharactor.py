class Solution(object):
    def numberOfWeakCharacters(self, properties):
        """
        :type properties: List[List[int]]
        :rtype: int
        """
        # Sort by attack desc, defense asc
        properties.sort(key=lambda x: (-x[0], x[1]))
        max_def = 0
        weak = 0
        for _, d in properties:
            if d < max_def:
                weak += 1
            else:
                max_def = d
        return weak
