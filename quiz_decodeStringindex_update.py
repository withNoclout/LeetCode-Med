# ...existing code...
class Solution(object):
    def decodeAtIndex(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        # compute length of decoded string until >= k
        size = 0
        for ch in s:
            if ch.isdigit():
                size *= int(ch)
            else:
                size += 1
            if size >= k:
                break

        # walk backward to find the k-th character
        for ch in reversed(s):
            if ch.isdigit():
                d = int(ch)
                size //= d
                if size:          # guard to avoid division/modulo by zero
                    k %= size
            else:
                if k == 0 or k == size:
                    return ch
                size -= 1
        return ""  # fallback (shouldn't happen)
