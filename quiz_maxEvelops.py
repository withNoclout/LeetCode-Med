import bisect

class Solution(object):
    def maxEnvelopes(self, envelopes):
        if not envelopes:
            return 0
            
        # 1. Sort: width asc, then height desc
        # envelopes.sort(key=lambda x: (x[0], -x[1]))
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        
        # 2. Find LIS on heights using binary search (Patience Sorting)
        lis = []
        for _, h in envelopes:
            # Find the index where h should be placed to maintain a sorted lis
            idx = bisect.bisect_left(lis, h)
            
            if idx == len(lis):
                # h is larger than all elements in lis, extend the sequence
                lis.append(h)
            else:
                # Replace the existing element at idx with h
                # This helps keep the sequence values as small as possible
                lis[idx] = h
                
        return len(lis)
