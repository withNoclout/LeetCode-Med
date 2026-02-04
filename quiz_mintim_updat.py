class Solution(object):
    def minTime(self, s, order, k):
        """
        :type s: str
        :type order: List[int]
        :type k: int
        :rtype: int
        """
        n = len(s)

        def isActiveAtTime(t):
            # Mark positions as stars up to time t
            is_star = [False] * n
            for i in range(t + 1):
                is_star[order[i]] = True
            
            invalid_count = 0
            segment_length = 0
            
            # Count invalid substrings (substrings with NO stars)
            # These are just contiguous segments of the original characters
            for i in range(n):
                if not is_star[i]:
                    segment_length += 1
                else:
                    invalid_count += (segment_length * (segment_length + 1)) // 2
                    segment_length = 0
            
            # Handle trailing segment
            if segment_length > 0:
                invalid_count += (segment_length * (segment_length + 1)) // 2
            
            total_substrings = n * (n + 1) // 2
            valid_substrings = total_substrings - invalid_count
            
            return valid_substrings >= k

        # Binary Search for the minimum time
        left, right = 0, n - 1
        answer = -1 # Default if not found, though problem constraints usually ensure a solution

        while left <= right:
            mid = (left + right) // 2
            
            if isActiveAtTime(mid):
                answer = mid
                right = mid - 1
            else:
                left = mid + 1
                
        return answer
