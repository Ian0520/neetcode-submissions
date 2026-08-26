class Twitter:

    def __init__(self):
        self.posts = {}
        self.follows = {}
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.posts:
            self.posts[userId] = [(tweetId, self.time)]
            self.time += 1
            if userId not in self.follows:
                self.follows[userId] = set([userId])
            else:
                self.follows[userId].append(userId)
        else:
            self.posts[userId].append((tweetId, self.time))
            self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        min_heap = []
        for followeeId in self.follows[userId]:
            for tweetId, time in self.posts[followeeId]:
                heapq.heappush(min_heap, (time, tweetId))
                if len(min_heap) > 10:
                    heapq.heappop(min_heap)
        result = []
        while min_heap:
            result.append(heapq.heappop(min_heap)[1])
        result.reverse()
        return result

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.follows:
            self.follows[followerId] = set([followeeId])
        else:
            self.follows[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId not in self.follows[followerId]:
            return
        self.follows[followerId].remove(followeeId)
