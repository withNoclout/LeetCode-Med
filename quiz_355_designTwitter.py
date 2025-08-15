import heapq
from collections import defaultdict

class Twitter:
    def __init__(self):
        self.time = 0
        self.tweets = defaultdict(list)      # userId -> list of (time, tweetId)
        self.following = defaultdict(set)    # userId -> set of followees

    def postTweet(self, userId: int, tweetId: int) -> None:
        # Always follow yourself so your own tweets appear in your feed
        self.following[userId].add(userId)
        self.time += 1
        self.tweets[userId].append((self.time, tweetId))

    def getNewsFeed(self, userId: int):
        self.following[userId].add(userId)  # Ensure self-follow
        heap = []
        for uid in self.following[userId]:
            arr = self.tweets[uid]
            if arr:
                t, tid = arr[-1]
                heapq.heappush(heap, (-t, uid, len(arr) - 1))  # max-heap by time

        res = []
        while heap and len(res) < 10:
            negt, uid, idx = heapq.heappop(heap)
            res.append(self.tweets[uid][idx][1])
            if idx - 1 >= 0:
                t, tid = self.tweets[uid][idx - 1]
                heapq.heappush(heap, (-t, uid, idx - 1))
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        # Can't unfollow yourself
        if followeeId != followerId:
            self.following[followerId].discard(followeeId)
