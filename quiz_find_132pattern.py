class Solution(object):
    def find132pattern(self, nums):
        stack = []
        third = float('-inf')  # candidate for "2" in 132

        for num in reversed(nums):
            if num < third:  # found "1"
                return True
            while stack and num > stack[-1]:
                third = stack.pop()  # update "2"
            stack.append(num)  # push candidate for "3"
        
        return False

