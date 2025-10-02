import requests
from fake_useragent import UserAgent


def getPosts(url, story_count=1):

    if ".json" not in url:
        url = url + ".json"

    data = requests.get(url, headers={"User-Agent": UserAgent().chrome}).json()


    results = []
    for story in range(story_count):
        post = data["data"]['children'][story]['data']
        title = post['title']
        text = post['selftext']
        postURL = post['url']

        results.append(
            {
                "title": title,
                "text": text,
                "URL": postURL
            }
        )
    return results







    






