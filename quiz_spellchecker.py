import math
class Solution(object):
    def spellchecker(self, wordlist, queries):
        """
        :type wordlist: List[str]
        :type queries: List[str]
        :rtype: List[str]
        """
        def devowel(word):
            return ''.join('*' if c in 'aeiou' else c for c in word)

        words = set(wordlist)
        lower_map = {}
        vowel_map = {}
        for word in wordlist:
            lw = word.lower()
            if lw not in lower_map:
                lower_map[lw] = word
            vw = devowel(lw)
            if vw not in vowel_map:
                vowel_map[vw] = word
        res = []
        for q in queries:
            if q in words:
                res.append(q)
            else:
                lq = q.lower()
                if lq in lower_map:
                    res.append(lower_map[lq])
                else:
                    vq = devowel(lq)
                    if vq in vowel_map:
                        res.append(vowel_map[vq])
                    else:
                        res.append("")
        return res
    def minAreaFreeRect(self, points):
        """
        :type points: List[List[int]]
        :rtype: float
        """
        point_set = set(map(tuple, points))
        n = len(points)
        min_area = float('inf')
        for i in range(n):
            x1, y1 = points[i]
            for j in range(n):
                if j == i: continue
                x2, y2 = points[j]
                for k in range(n):
                    if k == i or k == j: continue
                    x3, y3 = points[k]
                    vx1, vy1 = x2 - x1, y2 - y1
                    vx2, vy2 = x3 - x1, y3 - y1
                    if vx1 * vx2 + vy1 * vy2 != 0:
                        continue
                    x4, y4 = x2 + x3 - x1, y2 + y3 - y1
                    if (x4, y4) in point_set:
                        area = math.hypot(vx1, vy1) * math.hypot(vx2, vy2)
                        if area > 0:
                            min_area = min(min_area, area)
        return 0 if min_area == float('inf') else min_area
