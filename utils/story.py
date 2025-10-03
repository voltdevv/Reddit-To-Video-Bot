import requests
from fake_useragent import UserAgent


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

        data = requests.get(url, headers=self.ua).json()

        results = []

        while story_count <= 25: # max per request 
        
            post = data['data']['children'][story_count]['data']
            title = post['title']
            text = post['selftext']
            postURL = post['url']

            results.append(Post(title, text, postURL))
            story_count += 1 

        return results
    


