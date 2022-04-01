import requests
from bs4 import BeautifulSoup
import pprint


res = requests.get("https://news.ycombinator.com/news")
# res = requests.get("https://hacker-news.firebaseio.com/v0/item/8863.json?print=pretty")
# res = requests.get("https://www.bbc.co.uk/news")
soup = BeautifulSoup(res.text, "html.parser")
# print(dir(soup))
title_links = soup.select(".titlelink")
subtext = soup.select(".subtext")


def create_custom_hn(links, subtext):
    hn = []
    for idx, item in enumerate(links):
        title = links[idx].getText()
        href = links[idx].get("href", None)
        vote = subtext[idx].select(".score")
        if len(vote):
            points = int(vote[0].getText().replace(" points", ""))
            if points > 199:
                hn.append({"title": title, "link": href, "points": points})
    return sorted(hn, reverse=True, key=lambda x: x["points"])


# def lambda_custom_hn(links, subtext):
# return [
#     {
#         "title": x.getText(),
#         "link": x.get("href", None),
#         "points": list(p.select(".score"))[0].replace(" points", "MM"),
#     }
#     for x, p in zip(links, subtext)
#     if p.select(".score") is not None
# ]


pprint.pprint(create_custom_hn(title_links, subtext))
# print(lambda_custom_hn(title_links, subtext))
