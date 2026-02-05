import heapq

class Solution(object):
    def score(self, cards, x):
        """
        :type cards: List[str]
        :type x: str
        :rtype: int
        """
        cnt_xx = 0
        cnt1 = [0] * 26  # Counts for cards starting with x (X_)
        cnt2 = [0] * 26  # Counts for cards ending with x (_X)
        
        base = ord('a')
        
        for c in cards:
            if c[0] == x and c[1] == x:
                cnt_xx += 1
            elif c[0] == x:
                cnt1[ord(c[1]) - base] += 1
            elif c[1] == x:
                cnt2[ord(c[0]) - base] += 1
                
        def get_scores(counts):
            # Returns a list where list[k] is the max internal pairs 
            # possible after removing k elements optimally.
            pq = [-c for c in counts if c > 0]
            heapq.heapify(pq)
            
            curr_sum = sum(counts)
            history = []
            
            # Simulate removing elements one by one
            while curr_sum >= 0:
                if not pq:
                    history.append(0)
                    if curr_sum == 0:
                        break
                else:
                    max_freq = -pq[0]
                    # Calculate max internal pairs for current state
                    pairs = min(curr_sum // 2, curr_sum - max_freq)
                    history.append(pairs)
                    
                    if curr_sum == 0:
                        break
                        
                    # Remove one element from the most frequent type
                    curr_sum -= 1
                    pop = heapq.heappop(pq)
                    pop += 1 # Decrease count (magnitude decreases)
                    if pop < 0:
                        heapq.heappush(pq, pop)
            return history

        scores1 = get_scores(cnt1)
        scores2 = get_scores(cnt2)
        
        # We have cnt_xx "jokers" that act as bridges.
        # We must use min(cnt_xx, sum1 + sum2) of them to form pairs with S1 and S2.
        # Any excess "xx" cards cannot pair with themselves, so they are discarded.
        
        limit = min(cnt_xx, (len(scores1) - 1) + (len(scores2) - 1))
        ans = 0
        
        # Iterate over how many "xx" cards we assign to S1 (k1) vs S2 (k2)
        # k1 + k2 = limit
        
        start_k1 = max(0, limit - (len(scores2) - 1))
        end_k1 = min(limit, len(scores1) - 1)
        
        for k1 in range(start_k1, end_k1 + 1):
            k2 = limit - k1
            # Total Score = (Pairs formed by xx) + (Internal pairs of remaining S1) + (Internal pairs of remaining S2)
            current_total = limit + scores1[k1] + scores2[k2]
            if current_total > ans:
                ans = current_total
                
        return ans
