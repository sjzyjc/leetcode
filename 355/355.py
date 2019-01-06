from collections import defaultdict
import heapq
class Twitter(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.follows = defaultdict(set)
        self.posts = defaultdict(list)
        self.timer = itertools.count()

    def postTweet(self, userId, tweetId):
        """
        Compose a new tweet.
        :type userId: int
        :type tweetId: int
        :rtype: void
        """
        self.posts[userId].append((-next(self.timer), tweetId))
        
    def getNewsFeed(self, userId):
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        :type userId: int
        :rtype: List[int]
        """
        self.follows[userId].add(userId)
        feed = []
        
        for fid in self.follows[userId]:
            post = self.posts[fid]
            
            if not post:
                continue
                
            heapq.heappush(feed, (post[-1], fid, len(post) - 1))
            
        ans = []
        while feed and len(ans) < 10:
            post, fid, index = heapq.heappop(feed)
            ans.append(post[1])
            index -= 1
            
            if index < 0:
                continue
                
            heapq.heappush(feed, (self.posts[fid][index], fid, index))
        
        return ans
                        

    def follow(self, followerId, followeeId):
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: void
        """
        self.follows[followerId].add(followeeId)

    def unfollow(self, followerId, followeeId):
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: void
        """
        self.follows[followerId].discard(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)