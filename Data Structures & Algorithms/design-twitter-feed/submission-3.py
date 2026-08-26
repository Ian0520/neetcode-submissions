class Twitter:

    def __init__(self):
        self.posts = defaultdict(list)
        self.follows = defaultdict(set)
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.posts[userId].append((self.time, tweetId))
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        max_heap = []
        users = self.follows[userId] | {userId}
        for followeeId in users:
            tweets = self.posts.get(followeeId, [])

            if tweets:
                index = len(tweets) - 1
                time, tweetId = tweets[index]

                heapq.heappush(
                    max_heap,
                    (-time, tweetId, followeeId, index)
                )
        result = []

        while max_heap and len(result) < 10:
            neg_time, tweetId, followeeId, index = heapq.heappop(
                max_heap
            )

            result.append(tweetId)

            if index > 0:
                index -= 1
                time, previousTweetId = self.posts[followeeId][index]

                heapq.heappush(
                    max_heap,
                    (-time, previousTweetId, followeeId, index)
                )

        return result


    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.follows[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].discard(followeeId)
