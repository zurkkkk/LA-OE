class SocialMediaAccount:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def login(self):
        return f"{self.username} logged in."

    def post(self, content):
        return f"Posted: {content}"


class InstagramAccount(SocialMediaAccount):
    def __init__(self, username, password, number_of_followers):
        super().__init__(username, password)
        self.number_of_followers = number_of_followers

    def share_story(self, story_content):
        return f"Shared story: {story_content}"


class XAccount(SocialMediaAccount):
    def __init__(self, username, password, number_of_tweets):
        super().__init__(username, password)
        self.number_of_tweets = number_of_tweets

    def tweet(self, tweet_content):
        return f"Tweeted: {tweet_content}"


# Create instances and show output
insta_account = InstagramAccount("user_insta", "pass123", 500)
print(insta_account.login())
print(insta_account.post("Hello Instagram!"))
print(insta_account.share_story("My first story!"))

x_account = XAccount("user_x", "pass456", 150)
print(x_account.login())
print(x_account.tweet("Hello X!"))
