"""
Threads Scraper
- unfinished i will scrap this... try with a python wrapper
"""

from dotenv import load_dotenv
import os
import requests

load_dotenv()


def get_access_token() -> str:
    """
    This method returns the access token for the app
    :return:
    """
    payload = {

    }
    # token = requests.get()
    response = requests.get("https://graph.facebook.com/oauth/access_token", params={
        "client_id": os.getenv("CLIENT_ID"), "client_secret": os.getenv("CLIENT_SECRET"),
        "grant_type": "client_credentials"})
    return response


def fetch_threads_posts(topic: str, limit: int = 100) -> list[list]:
    """
    This method fetches posts from threads related to the given topic

    :param topic:
    :param limit:
    :return: a list of different information relating to posts
    """
    payload = {"q": topic,
               "search_type": "TOP",
               "fields": "id,text,media_type,permalink,timestamp,username,has_replies,is_quote_post,is_reply",
               "access_token": os.getenv("")}
    response = requests.get("https://graph.threads.net/v1.0/keyword_search", params=payload)
    return response

    # ".../keyword_search/q=" + topic)
