import time
class Twitter:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.db = dict()

    def createUser(self, userId: int) -> None:
        basic = dict()
        basic["tweets"] = []
        basic["following"] = []
        self.db[userId] = basic


    def postTweet(self, userId: int, tweetId: int) -> None:
        """
        Compose a new tweet.
        Tweet form : (tweetId, timestamp)
        ex) object.postTweet(1,5) -> [(5, 1594994021.252249)]
        """
        tweet = (tweetId, time.time())
        if self.db.get(userId) != None:
            # User exists
            self.db[userId]["tweets"].append(tweet)
        else:
            # User doesn't exist. Create User
            self.createUser(userId)
            self.db[userId]["tweets"].append(tweet)
        

    def getNewsFeed(self, userId: int) -> List[int]:
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        """
        user = self.db.get(userId)
        
        if user == None:
            # Invalid User!
            return []
        
        follower = user.get("following")
        user_tweets = list(self.db[userId]["tweets"])
        follower_tweets = []

        if follower:
            for i in follower:
                tmp_user = self.db.get(i)
                if tmp_user != None:
                    tweets = list(tmp_user.get("tweets"))
                    follower_tweets += [t for t in tweets]
        
        total_tweets = user_tweets + follower_tweets
        total_tweets.sort(key=lambda x:x[1], reverse=True)
        
        return [i[0] for i in total_tweets[:10]]
            
        

    def follow(self, followerId: int, followeeId: int) -> None:
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        """
        if (self.db.get(followerId) == None):
            # User doesn't exist. Create User (This doesn't make sense)
            self.createUser(followerId)
            self.db[followerId]["following"].append(followeeId)
            return None
            
        
        if followeeId in self.db[followerId]["following"]:
            # Invalid Operation
            return None
        
        if followerId == followeeId:
            # Invalid Operation
            return None
        
        
        self.db[followerId]["following"].append(followeeId)
        if (self.db.get(followeeId) == None):
            # User doesn't exist. Create User
            return self.createUser(followeeId)
        
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        """
        if (self.db.get(followerId) == None) or (self.db.get(followeeId) == None):
            # Invalid Operation
            return None
        
        if followeeId in self.db[followerId]["following"]:
            self.db[followerId]["following"].remove(followeeId)
        else:
            # Invalid Operation
            return None
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)