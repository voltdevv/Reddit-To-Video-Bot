import requests
from fake_useragent import UserAgent


class Post:

    def __init__(self, title, text, url):
        self.title = title
        self.text = text
        self.url = url


def GetPosts(url, story_count=1):

    if ".json" not in url:
        url = url + ".json"

    data = requests.get(url, headers={"User-Agent": UserAgent().chrome}).json()

    results = []

    for story in range(story_count):
        
        post = data['data']['children'][story]['data']
        title = post['title']
        text = post['selftext']
        postURL = post['url']

        results.append(Post(title, text, postURL))

    return results


