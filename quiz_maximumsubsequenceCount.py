class Solution(object):
    def maximumSubsequenceCount(self, text, pattern):
        a, b = pattern[0], pattern[1]
        if a == b:
            cnt = text.count(a) + 1  # insert one more 'a'
            return (cnt * (cnt - 1)) // 2

        cnt_a = 0
        base = 0
        for ch in text:
            if ch == a:
                cnt_a += 1
            if ch == b:
                base += cnt_a

        cnt_b = text.count(b)
        # Insert 'a' at start gives +cnt_b; insert 'b' at end gives +cnt_a
        return base + max(cnt_b, cnt_a)
