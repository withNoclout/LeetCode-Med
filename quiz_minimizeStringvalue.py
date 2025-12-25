class Solution(object):
    def minimizeStringValue(self, s):
        import heapq
        
        # Count existing non-'?' characters
        cnt = [0] * 26
        for c in s:
            if c != '?':
                cnt[ord(c) - ord('a')] += 1
        
        # Priority queue to keep track of character frequencies: (freq, char_index)
        pq = [(cnt[i], i) for i in range(26)]
        heapq.heapify(pq)
        
        # Determine the set of characters to add
        fill_chars = []
        k = s.count('?')
        for _ in range(k):
            freq, idx = heapq.heappop(pq)
            fill_chars.append(chr(ord('a') + idx))
            heapq.heappush(pq, (freq + 1, idx))
            
        # Sort characters to ensure the resulting string is lexicographically smallest
        fill_chars.sort()
        
        # Reconstruct the string
        res = []
        fill_idx = 0
        for c in s:
            if c == '?':
                res.append(fill_chars[fill_idx])
                fill_idx += 1
            else:
                res.append(c)
                
        return "".join(res)
