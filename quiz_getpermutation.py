class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        # Create a list of available numbers as strings
        numbers = [str(i) for i in range(1, n + 1)]
        
        # Precompute factorials up to n
        fact = [1] * n
        for i in range(1, n):
            fact[i] = fact[i - 1] * i
            
        # Convert k to 0-indexed to make the math work cleanly
        k -= 1
        result = []
        
        # Find the correct number for each of the n positions
        for i in range(n - 1, -1, -1):
            # Calculate which block k falls into
            index = k // fact[i]
            
            # Pick the number, add to result, and remove from available pool
            result.append(numbers.pop(index))
            
            # Update k for the next iteration (the remainder)
            k %= fact[i]
            
        return "".join(result)
