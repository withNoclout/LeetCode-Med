class Solution(object):
    def minOperations(self, s, k):
        n = len(s)
        zeros = s.count('0')
        
        if zeros == 0:
            return 0
            
        if k == 0:
            return -1
            
        max_ops = n + 5
        
        for ops in range(1, max_ops + 1):
            total_flips = ops * k
            if total_flips < zeros:
                continue
            if (total_flips - zeros) % 2 != 0:
                continue
                
            y = (total_flips - zeros) // 2
            x = total_flips - y
            
            if x <= ops * n and y <= ops * n:
                max_zeros_can_flip = min(zeros, n) * ops 
                if ops == 1:
                    if x == zeros and y == 0:
                        return 1
                else:
                    max_ones_can_flip = (n - zeros) * ops
                    valid = True
                    for char in s:
                        if char == '0':
                            if x == 0: valid = False
                        else:
                            pass 
                    
                    if x <= zeros * ops and y <= (n - zeros) * ops + (zeros * ops - x):
                        pass

        from collections import deque
        q = deque([(zeros, 0)])
        visited = {zeros}
        
        while q:
            curr_zeros, ops = q.popleft()
            
            if curr_zeros == 0:
                return ops
                
            if ops > n + 2:
                break
                
            curr_ones = n - curr_zeros
            
            min_flip_zeros = max(0, k - curr_ones)
            max_flip_zeros = min(curr_zeros, k)
            
            for flip_zeros in range(min_flip_zeros, max_flip_zeros + 1):
                flip_ones = k - flip_zeros
                next_zeros = curr_zeros - flip_zeros + flip_ones
                
                if next_zeros not in visited:
                    visited.add(next_zeros)
                    q.append((next_zeros, ops + 1))
                    
        return  -1 
