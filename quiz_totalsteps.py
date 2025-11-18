class Solution(object):
    def totalSteps(self, nums):
        stack = []  # each element: [value, steps needed to remove]
        res = 0

        for num in nums:
            steps = 0
            while stack and num >= stack[-1][0]:
                steps = max(steps, stack.pop()[1])
            if stack:
                steps += 1
            else:
                steps = 0
            res = max(res, steps)
            stack.append([num, steps])
        
        return res
