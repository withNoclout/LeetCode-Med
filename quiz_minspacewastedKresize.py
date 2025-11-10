class Solution(object):
    def minimumBuckets(self, hamsters):
        """
        :type hamsters: str
        :rtype: int
        """
        s = list(hamsters)
        n = len(s)
        buckets = 0

        for i in range(n):
            if s[i] != 'H':
                continue

            # Already covered by a bucket on the left
            if i > 0 and s[i - 1] == 'B':
                continue

            # Prefer placing a bucket to the right (greedy to not block next house)
            if i + 1 < n and s[i + 1] == '.':
                s[i + 1] = 'B'
                buckets += 1
                continue

            # Otherwise, try placing to the left
            if i - 1 >= 0 and s[i - 1] == '.':
                s[i - 1] = 'B'
                buckets += 1
                continue

            # No place to put a bucket for this house
            return -1

        return buckets
