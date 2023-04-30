from apis.reddit.reddit_posts import RedditPosts
from apis.io.post_io import load_posts, save_posts
import datatable as dt
import pandas as pd

import logging

logger = logging.getLogger(__name__)

NEW_POSTS_LISTING = "new"
TOP_POSTS_LISTING = "top"

NEW_POSTS_COUNT = 100
TOP75_POSTS_COUNT = 75

POST_COLUMNS = [
    "author_fullname",
    "title",
    "name",
    "score",
    "created",
    "view_count",
    "id",
    "author",
    "url",
    "created_utc"
    ]

POST_COLUMNS_X = {POST_COLUMNS[i]+"_x":POST_COLUMNS[i] for i in range(len(POST_COLUMNS))}
POST_COLUMNS_Y = {POST_COLUMNS[i]+"_y":POST_COLUMNS[i] for i in range(len(POST_COLUMNS))}


""" The Reddit posts processor

get redit posts as json from reddit.com
load posts from last execution
save posts to disk (for next execution)
use dataframes to compare latest posts against last program run
"""
class RedditProcessor:
    
    
    def __init__(self):
        self.reddit_new = RedditPosts(listing=NEW_POSTS_LISTING, limit=NEW_POSTS_COUNT, timeframe="hour")
        self.reddit_top = RedditPosts(listing=TOP_POSTS_LISTING, limit=TOP75_POSTS_COUNT, timeframe="hour")
        self.df_new_posts = self.load_posts(self.reddit_new, NEW_POSTS_LISTING)
        self.df_top_posts = self.load_posts(self.reddit_top, TOP_POSTS_LISTING)


    def load_posts(self, reddit_posts, listing ):
        logger.info(f"====> {listing} POSTS:")
        latest_posts = reddit_posts.load(columns=POST_COLUMNS)
        logging.info(f"latest {listing} posts count {latest_posts.nrows}")

        previous_posts = load_posts(listing=listing, columns=POST_COLUMNS)
        logging.info(f"previous {listing} posts count {previous_posts.nrows}")    

        # save for next program execution
        save_posts(listing=listing, posts=latest_posts)

        # use pandas to merge into a single dataframe with all posts from latest and previous exeuction
        df_latest = latest_posts.to_pandas()
        df_previous = previous_posts.to_pandas()
        df = pd.merge(df_latest, df_previous, on=['id'], how="outer", indicator=True)
        return df


    def get_new_posts(self):
        df_new_since_last = self.df_new_posts[self.df_new_posts['_merge'] == 'left_only']
        df_new_since_last = df_new_since_last.rename(POST_COLUMNS_X, axis=1)
        df_new_since_last = df_new_since_last[POST_COLUMNS]
        logger.info(f"============> {df_new_since_last.shape[0]} LATEST NEW POSTS")
        logger.info(df_new_since_last[['id','created_utc','score']].head)
        return df_new_since_last
      
        
    def get_not_top75_posts(self):
        df_no_longer_top75 = self.df_top_posts[self.df_top_posts['_merge'] == 'right_only']
        df_no_longer_top75 = df_no_longer_top75.rename(POST_COLUMNS_Y, axis=1)
        df_no_longer_top75 = df_no_longer_top75[POST_COLUMNS]
        
        logger.info(f"============> {df_no_longer_top75.shape[0]} POSTS NO LONGER TOP 75")
        logger.info(df_no_longer_top75[['id','created_utc','score']].head)
        return df_no_longer_top75
    
    
    def get_scores_changed_posts(self):
        df_scores = pd.concat([self.df_top_posts, self.df_new_posts])
        df_scores.drop_duplicates(subset=['id'])

        df_scores = df_scores[(df_scores['_merge'] == 'both') & (df_scores['score_x'] != df_scores['score_y'])]

        df_scores = df_scores.rename(POST_COLUMNS_X, axis=1)
        df_scores = df_scores[POST_COLUMNS+['score_y']]
        df_scores['score_change'] = df_scores.score - df_scores.score_y
        
        logger.info(f"============> {df_scores.shape[0]} POSTS WITH SCORE CHANGES")
        logger.info(df_scores[['id','score','score_y','score_change']])
        return df_scores
