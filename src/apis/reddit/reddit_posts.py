from .reddit_api import get_posts
import datatable as dt
import logging

logger = logging.getLogger(__name__)
# logger.setLevel(logging.DEBUG)

"""
limit = 100 or less
timeframe = hour, day, week, month, year, all
listing = controversial, best, hot, new, random, rising, top
subreddit = 'python' or another subreddit
"""
class RedditPosts:

  def __init__(self, listing, limit, timeframe, subreddit=None):
    self.listing = listing
    self.limit = limit
    self.timeframe = timeframe
    self.subreddit = subreddit


  def load(self, columns):
    """loads posts from reddit and returns as datatable Frame for specified columns"""
    self.posts_json = get_posts(self.listing, self.limit, self.timeframe, self.subreddit)
    logger.debug(f"Received {len(self.posts_json['data']['children'])} {self.listing} posts from Reddit")
    result_df = self.filter_columns(columns)
    return result_df


  def filter_columns(self, columns):
    """return only the selected fields from "data" element under each post under json["data"]["children].  Result is a dict keyed by post["data"]["id"]"""
    filtered_posts = []
    for post in self.posts_json["data"]["children"]:
        filtered_post = {}
        if columns:
            for column in columns:
                filtered_post[column] = post["data"][column]
            filtered_posts.append(filtered_post)
        else:
            filtered_posts.append(post["data"])

    result = dt.Frame(filtered_posts, names=columns)
    logger.debug(f"{self.listing} POSTS DF={result}")

    return result
