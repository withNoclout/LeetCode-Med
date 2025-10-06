import heapq

class Solution(object):
    def avoidFlood(self, rains):
        """
        :type rains: List[int]
        :rtype: List[int]
        """
        lake_full = {}
        dry_days = []
        res = [-1] * len(rains)

        for i, lake in enumerate(rains):
            if lake == 0:
                heapq.heappush(dry_days, i)
                res[i] = 1  # placeholder
            else:
                if lake in lake_full:
                    if not dry_days:
                        return []
                    # Find a dry day before next rain of this lake
                    j = -1
                    for idx, d in enumerate(dry_days):
                        if d > lake_full[lake]:
                            j = idx
                            break
                    if j == -1:
                        return []
                    dry_day = dry_days[j]
                    res[dry_day] = lake
                    del dry_days[j]
                lake_full[lake] = i
                res[i] = -1
        return res
