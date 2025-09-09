# ...existing code...
class Solution(object):
    def sumSubarrayMins(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        MOD = 10**9 + 7
        n = len(arr)
        if n == 0:
            return 0

        # prev less (strict): index of previous element < arr[i]
        prev = [-1] * n
        stack = []
        for i in range(n):
            while stack and arr[stack[-1]] > arr[i]:
                stack.pop()
            prev[i] = stack[-1] if stack else -1
            stack.append(i)

        # next less or equal: index of next element < = arr[i]
        nxt = [n] * n
        stack = []
        for i in range(n - 1, -1, -1):
            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()
            nxt[i] = stack[-1] if stack else n
            stack.append(i)

        ans = 0
        for i in range(n):
            left = i - prev[i]
            right = nxt[i] - i
            ans = (ans + arr[i] * left * right) % MOD

        return ans
