import re
from datetime import datetime

import requests
import yaml
from bs4 import BeautifulSoup as Soup
from medium import Client
from scholarly import scholarly

google_scholar_id = "rSJ_vnYAAAAJ"
github_username = "tslmy"
medium_about = "https://lmy.medium.com/about"

if __name__ == "__main__":
    author = scholarly.search_author_id(google_scholar_id)
    scholarly_info = scholarly.fill(author, sections=["basics", "indices"])
    github_info = requests.get(f"https://api.github.com/users/{github_username}").json()

    data = {
        "hindex": scholarly_info["hindex"],
        "github_followers": github_info["followers"],
        "updated": datetime.now(),
    }

    response = requests.get(medium_about)
    text = response.text
    p = re.compile(r"(\d+) Followers")
    m = p.search(text)
    if m:
        num_followers = int(m.groups()[0])
        data["medium_followers"] = num_followers

    with open("_data/metrics.yaml", "w") as f:
        data_as_yaml = yaml.dump(data)
        f.write(data_as_yaml)
