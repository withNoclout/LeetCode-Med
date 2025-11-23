class Solution(object):
    def totalCost(self, costs, k, candidates):
        import heapq
        n = len(costs)
        head = costs[:candidates]
        tail = costs[max(candidates, n - candidates):]
        heapq.heapify(head)
        heapq.heapify(tail)
        
        ans = 0
        i = candidates
        j = n - candidates - 1
        
        for _ in range(k):
            if not tail or (head and head[0] <= tail[0]):
                ans += heapq.heappop(head)
                if i <= j:
                    heapq.heappush(head, costs[i])
                    i += 1
            else:
                ans += heapq.heappop(tail)
                if i <= j:
                    heapq.heappush(tail, costs[j])
                    j -= 1
        return ans
