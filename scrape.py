from datetime import datetime

import requests
import yaml
from scholarly import scholarly

google_scholar_id = "rSJ_vnYAAAAJ"
github_username = "tslmy"

if __name__ == "__main__":
    author = scholarly.search_author_id(google_scholar_id)
    scholarly_info = scholarly.fill(author, sections=["basics", "indices"])
    github_info = requests.get(f"https://api.github.com/users/{github_username}").json()

    data = {
        "hindex": scholarly_info["hindex"],
        "github_followers": github_info["followers"],
        "updated": datetime.now(),
    }

    with open("_data/metrics.yaml", "w") as f:
        data_as_yaml = yaml.dump(data)
        f.write(data_as_yaml)
