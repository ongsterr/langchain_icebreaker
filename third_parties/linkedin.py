import requests
import configparser
import json

config = configparser.ConfigParser()
config.read("config.ini")
proxycurl_api = json.loads(config.get("credentials", "proxycurl"))


def scrape_linkedin_profile(linkedin_profile_url: str, mock: bool = False):
    if mock:
        linkedin_profile_url = "https://gist.githubusercontent.com/emarco177/0d6a3f93dd06634d95e46a2782ed7490/raw/fad4d7a87e3e934ad52ba2a968bad9eb45128665/eden-marco.json"
        response = requests.get(linkedin_profile_url, timeout=10)
    else:
        api_endpoint = "https://nubela.co/proxycurl/api/v2/linkedin"
        proxycurl_api_key = proxycurl_api["api_key"]
        headers = {"Authorization": f"Bearer {proxycurl_api_key}"}
        response = requests.get(api_endpoint, params={"url": linkedin_profile_url}, headers=headers, timeout=10)

    data = response.json()
    data = {
        k: v
        for k, v in data.items()
        if v not in ([], "", "", None) and k not in ["people_also_viewed", "vertifications"]
    }
    if data.get("groups"):
        for group_dict in data.get("groups"):
            group_dict.pop("profile_pic_url")

    return data


if __name__ == "__main__":
    res = scrape_linkedin_profile(linkedin_profile_url="https://www.linkedin.com/in/chrisongg/", mock=True)
