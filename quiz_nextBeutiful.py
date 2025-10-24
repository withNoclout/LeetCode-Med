class Solution(object):
    def nextBeautifulNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        # upper bound on digits in the answer
        max_len = len(str(n)) + 1

        # collect all beautiful numbers with length <= max_len
        beauties = set()

        # choose which digits (1..9) to include; each chosen digit d appears exactly d times
        def choose_digits(d, curr_sum, counts):
            if curr_sum > max_len:
                return
            if d == 10:
                if 1 <= curr_sum <= max_len:
                    # build all permutations for this multiset 'counts'
                    build_numbers(counts, curr_sum)
                return

            # option 1: skip digit d
            choose_digits(d + 1, curr_sum, counts)

            # option 2: include digit d exactly d times (if it fits)
            if curr_sum + d <= max_len:
                counts[d] = d
                choose_digits(d + 1, curr_sum + d, counts)
                del counts[d]

        # backtrack to generate unique permutations (no leading zero; we never use zero anyway)
        def build_numbers(counts, total_len):
            digits = sorted(counts.keys(), reverse=False)  # order doesn't matter; we handle via counts
            curr = []

            def dfs():
                if len(curr) == total_len:
                    # form integer
                    val = 0
                    for ch in curr:
                        val = val * 10 + ch
                    beauties.add(val)
                    return
                for d in counts:
                    if counts[d] == 0:
                        continue
                    # no leading zero issue here (we never include digit 0)
                    counts[d] -= 1
                    curr.append(d)
                    dfs()
                    curr.pop()
                    counts[d] += 1

            dfs()

        choose_digits(1, 0, {})

        # find the smallest beautiful number strictly greater than n
        candidates = sorted(beauties)
        # there will always be an answer since e.g. 111111111 (nine 1's) etc.
        import bisect
        i = bisect.bisect_right(candidates, n)
        return candidates[i]
