class Solution(object):
    def wordCount(self, startWords, targetWords):
        def mask(word):
            m = 0
            for ch in word:
                m |= 1 << (ord(ch) - 97)
            return m

        start_masks = set(mask(w) for w in startWords)

        ans = 0
        for t in targetWords:
            mt = mask(t)
            found = False
            for ch in t:
                bit = 1 << (ord(ch) - 97)
                if mt & bit and (mt ^ bit) in start_masks:
                    ans += 1
                    found = True
                    break
            # if not found, continue to next target
        return ans
