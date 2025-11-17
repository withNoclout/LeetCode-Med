class Solution(object):
    def maximumWhiteTiles(self, tiles, carpetLen):
        """
        :type tiles: List[List[int]]
        :type carpetLen: int
        :rtype: int
        """
        tiles.sort()
        n = len(tiles)
        res = 0
        cover = 0
        j = 0

        for i in range(n):
            start = tiles[i][0]
            end_carpet = start + carpetLen - 1

            while j < n and tiles[j][1] <= end_carpet:
                cover += tiles[j][1] - tiles[j][0] + 1
                j += 1

            partial = 0
            if j < n and tiles[j][0] <= end_carpet:
                partial = end_carpet - tiles[j][0] + 1

            res = max(res, cover + partial)

            cover -= tiles[i][1] - tiles[i][0] + 1

        return res
