class SummaryRanges:
    def __init__(self):
        self.seen=set()

    def addNum(self, val):
        self.seen.add(val)

    def getIntervals(self):
        res=[]
        for v in sorted(self.seen):
            if not res or v>res[-1][1]+1:
                res.append([v,v])
            elif res and v==res[-1][1]+1:
                res[-1][1]=v
        return res
