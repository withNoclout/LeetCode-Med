class TopVotedCandidate(object):

    def __init__(self, persons, times):
        """
        :type persons: List[int]
        :type times: List[int]
        """
        from collections import defaultdict 

        self.times = times 
        self.leaders = [] 
        cnt = defaultdict(int) 
        leader = -1 
        leader_votes =  0 
        for p in persons : 
            cnt[p] += 1 
            if cnt[p] >= leader_votes : 
                leader = p 
                leader_votes = cnt[p] 
            self.leaders.append(leader ) 

        

    def q(self, t):
        """
        :type t: int
        :rtype: int
        """
        import bisect 
        idx = bisect.bisect_right(self.times, t)
        return self.leaders[idx - 1] if idx > 0 else -1
    


# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)
