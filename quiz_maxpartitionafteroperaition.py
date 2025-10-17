from collections import defaultdict

class Solution(object):
    def maxPartitionsAfterOperations(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        # Greedy baseline: number of partitions without any change.
        # While building each partition, also record whether:
        #  - the partition already uses exactly k distinct letters, and
        #  - it contains some letter with frequency >= 2
        # If both hold (and there exists a letter outside this partition
        #  to switch to), then a single character change can make this
        #  partition overflow earlier, yielding +1 partition in total.
        if k == 26:  # cannot create k+1 distinct letters
            # Baseline greedy partitions is already maximal.
            cnt = [0]*26
            distinct = 0
            parts = 1 if s else 0
            for ch in s:
                idx = ord(ch) - 97
                if cnt[idx] == 0 and distinct == k:
                    # start new part
                    parts += 1
                    cnt = [0]*26
                    distinct = 0
                if cnt[idx] == 0:
                    distinct += 1
                cnt[idx] += 1
            return parts

        parts = 0
        i = 0
        can_gain = False

        n = len(s)
        while i < n:
            freq = defaultdict(int)
            distinct = 0
            has_dup = False
            j = i
            while j < n:
                c = s[j]
                if freq[c] == 0 and distinct == k:
                    break  # adding c would exceed k -> close partition before j
                if freq[c] == 0:
                    distinct += 1
                freq[c] += 1
                if freq[c] == 2:
                    has_dup = True
                j += 1

            parts += 1
            # If this partition ended because the next char would overflow,
            # then it currently has exactly k distinct letters.
            # With one change inside this partition:
            #  - change some character whose letter appears >=2 times
            #  - to a letter NOT in this partition
            # This increases distinct count by +1 earlier -> one extra partition.
            if distinct == k and has_dup and distinct < 26:
                can_gain = True

            i = j  # start next partition

        return parts + (1 if can_gain else 0)
