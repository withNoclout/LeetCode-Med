class Solution(object):
    def maximumSumOfHeights(self, heights):
        n = len(heights)
        left = [0] * n
        stack = [-1] # Monotonic stack storing indices
        
        # Calculate max sum for increasing sequence ending at i
        for i in range(n):
            while len(stack) > 1 and heights[stack[-1]] > heights[i]:
                stack.pop()
            
            if stack[-1] == -1:
                left[i] = heights[i] * (i + 1)
            else:
                left[i] = left[stack[-1]] + heights[i] * (i - stack[-1])
            stack.append(i)
            
        right = [0] * n
        stack = [n]
        
        # Calculate max sum for decreasing sequence starting at i
        for i in range(n - 1, -1, -1):
            while len(stack) > 1 and heights[stack[-1]] > heights[i]:
                stack.pop()
                
            if stack[-1] == n:
                right[i] = heights[i] * (n - i)
            else:
                right[i] = right[stack[-1]] + heights[i] * (stack[-1] - i)
            stack.append(i)
            
        return max(left[i] + right[i] - heights[i] for i in range(n))
