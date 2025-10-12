class Solution(object):
    def magicalSum(self, m, k, nums):
        """
        :type m: int
        :type k: int
        :type nums: List[int]
        :rtype: int
        """
        MOD = 10**9 + 7
        n = len(nums)

        # Precompute nCk up to m
        C = [[0]*(m+1) for _ in range(m+1)]
        for i in range(m+1):
            C[i][0] = C[i][i] = 1
            for j in range(1, i):
                C[i][j] = (C[i-1][j-1] + C[i-1][j]) % MOD

        # Precompute powers for each nums[i] up to m
        powv = []
        for v in nums:
            arr = [1]*(m+1)
            for t in range(1, m+1):
                arr[t] = (arr[t-1] * v) % MOD
            powv.append(arr)

        from collections import defaultdict

        # dp state: (used, carry, popcount_so_far) -> value
        dp = defaultdict(int)
        dp[(0, 0, 0)] = 1

        for i in range(n):
            ndp = defaultdict(int)
            pv = powv[i]
            # For each state, choose t times index i appears
            for (used, carry, pc), ways in dp.items():
                rem = m - used
                if rem < 0:
                    continue
                # If current minimal possible pc already exceeds k, skip
                if pc > k:
                    continue
                for t in range(rem + 1):
                    # choose t positions for index i
                    choose = C[rem][t]
                    val = ways * choose % MOD
                    val = val * pv[t] % MOD

                    s = carry + t
                    bit = s & 1
                    ncarry = s >> 1
                    npc = pc + bit
                    if npc > k:
                        continue
                    nused = used + t
                    ndp[(nused, ncarry, npc)] = (ndp[(nused, ncarry, npc)] + val) % MOD
            dp = ndp

        # finalize: use only states with used == m, add remaining carry's popcount to pc
        def popcount(x):
            return bin(x).count("1")

        ans = 0
        for (used, carry, pc), ways in dp.items():
            if used != m:
                continue
            total_pc = pc + popcount(carry)
            if total_pc == k:
                ans = (ans + ways) % MOD
        return ans

