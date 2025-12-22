class Solution(object):
    def findHighAccessEmployees(self, access_times):
        import collections
        d = collections.defaultdict(list)
        for name, t in access_times:
            d[name].append(int(t[:2]) * 60 + int(t[2:]))
            
        res = []
        for name, times in d.items():
            times.sort()
            for i in range(len(times) - 2):
                if times[i+2] - times[i] < 60:
                    res.append(name)
                    break
        return res
