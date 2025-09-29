import collections
import bisect

class TweetCounts(object):

    def __init__(self):
        # store tweets per name, keep sorted times
        self.tweets = collections.defaultdict(list)

    def recordTweet(self, tweetName, time):
        """
        :type tweetName: str
        :type time: int
        :rtype: None
        """
        # insert in sorted order
        bisect.insort(self.tweets[tweetName], time)

    def getTweetCountsPerFrequency(self, freq, tweetName, startTime, endTime):
        """
        :type freq: str
        :type tweetName: str
        :type startTime: int
        :type endTime: int
        :rtype: List[int]
        """
        if freq == "minute":
            interval = 60
        elif freq == "hour":
            interval = 3600
        else:  # "day"
            interval = 86400

        times = self.tweets[tweetName]
        res = []
        # number of buckets
        n = (endTime - startTime) // interval + 1
        res = [0] * n

        # get relevant range of times
        left = bisect.bisect_left(times, startTime)
        right = bisect.bisect_right(times, endTime)

        for t in times[left:right]:
            idx = (t - startTime) // interval
            res[idx] += 1

        return res
