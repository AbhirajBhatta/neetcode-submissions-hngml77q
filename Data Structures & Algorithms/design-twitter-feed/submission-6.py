class Twitter:

    def __init__(self):
        self.time = 0
        self.tweetmap = defaultdict(list)
        self.followeemap = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetmap[userId].append((-1*self.time, tweetId))
        self.time+=1

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        heap = []
        self.followeemap[userId].add(userId)
        for followeeId in self.followeemap[userId]:
            if followeeId in self.tweetmap:
                idx = len(self.tweetmap[followeeId])-1
                time, tweetId = self.tweetmap[followeeId][idx]
                heap.append([time, tweetId, followeeId, idx-1])
        heapq.heapify(heap)
        while heap and len(res)<10:
            time, tweetId, followeeId, idx = heapq.heappop(heap)
            res.append(tweetId)
            if idx>=0:
                time, tweetId = self.tweetmap[followeeId][idx]
                heapq.heappush(heap, [time, tweetId, followeeId, idx-1])
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followeemap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followeemap[followerId]:
            self.followeemap[followerId].remove(followeeId)
