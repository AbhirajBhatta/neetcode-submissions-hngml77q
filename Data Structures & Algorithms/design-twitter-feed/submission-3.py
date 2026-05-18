class Twitter:

    def __init__(self):
        self.count = 0
        self.foloweeMap = defaultdict(set)
        self.tweetMap = defaultdict(list)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append([self.count, tweetId])
        self.count -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        heap = []
        self.foloweeMap[userId].add(userId)
        for folowee in self.foloweeMap[userId]:
            if folowee in self.tweetMap:
                index = len(self.tweetMap[folowee])-1
                count, tweetId = self.tweetMap[folowee][index]
                heap.append([count, tweetId, folowee, index-1])
        heapq.heapify(heap)
        while heap and len(res) < 10:
            count, tweetId, folowee, index = heapq.heappop(heap)
            res.append(tweetId)
            if index >= 0:
                count, tweetId = self.tweetMap[folowee][index] 
                heapq.heappush(heap, [count, tweetId, folowee, index-1])
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.foloweeMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.foloweeMap[followerId]:
            self.foloweeMap[followerId].remove(followeeId)
