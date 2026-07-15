class Twitter:
    def __init__(self):
        self.relations = defaultdict(set)
        self.posts = defaultdict(list)
        self.count = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.count += 1
        self.posts[userId].append([self.count, tweetId])

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        max_heap = []

        followed_users = set(self.relations[userId])
        followed_users.add(userId)

        for followeeId in followed_users:
            for order, tweetId in self.posts[followeeId]:
                heapq.heappush_max(max_heap, [order, tweetId])

        n = 10
        while max_heap and n > 0:
            _, tweetId = heapq.heappop_max(max_heap)
            res.append(tweetId)
            n -= 1

        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.relations[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.relations:
            self.relations[followerId].discard(followeeId)
