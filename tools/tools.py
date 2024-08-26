from langchain_community.tools.tavily_search import TavilySearchResults

from dotenv import load_dotenv
import os

load_dotenv()


def get_profile_url_tavily(name: str):
    search = TavilySearchResults()
    res = search.run(f"{name}")
    return res[0]["url"]  # only return first result
