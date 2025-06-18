import praw
import os
from dotenv import load_dotenv

load_dotenv()


def fetch_reddit_posts(topic: str, limit: int = 100) -> list:
    """
    Fetches recent Reddit posts related to a given topic.
    Args:
        topic (str): The topic to search for on Reddit.
        limit (int): The maximum number of posts to retrieve. Default is 20.
    """
    reddit = praw.Reddit(
        client_id=os.getenv("REDDIT_CLIENT_ID"),
        client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
        user_agent="PolarBear",
        username=os.getenv("REDDIT_USERNAME"),
        password=os.getenv("REDDIT_PASSWORD"),
    )
    results = []
    for post in reddit.subreddit("all").search(topic, limit=limit, sort="hot"):
        results.append(
            {
                "title": post.title,
                "text": post.selftext,
                "timestamp": post.created_est,
                "url": post.url,
                "score": post.score,
                "subreddit": post.subreddit.display_name,
            }
        )

    return results
