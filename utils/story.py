import requests
from fake_useragent import UserAgent
import os

class Post:

    def __init__(self, title, text, url):
        self.title = title
        self.text = text
        self.url = url


class Scraper:

    def __init__(self):
        self.ua = UserAgent().chrome
        

    def get(self, url, story_count=1):

        if ".json" not in url:
            url += ".json"

        data = requests.get(url, headers={"User-Agent": self.ua}).json()

        results = []

        for story in range(story_count): # max per request 
        
            post = data['data']['children'][story]['data']
            title = post['title']
            text = post['selftext']
            postURL = post['url']

            results.append(Post(title, text, postURL))

        return results
    
    def filter(self, text):
        pass



