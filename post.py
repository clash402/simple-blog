import requests as req


class Post:
    def __init__(self):
        self.URL = "https://api.npoint.io/5abcca6f4e39b4955965"

    def get_posts(self):
        return req.get(self.URL).json()
