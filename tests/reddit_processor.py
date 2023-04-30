import unittest
from reddit_posts.src.reddit_processor import RedditProcessor
import reddit_processor

import datatable as dt

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

class TestLoadReddit(unittest.TestCase):
    def test_load_posts_success(self):
        actual ={"tank_a": ["shark", "tuna"]}
        expected = {"tank_a": ["shark", "tuna"]}
        
        
        
        self.assertEqual(actual, expected)
        
    def test_detect_new_posts_success(self):        
        lastest_new_posts_data = [
            ("author 1","title 1","name 1",101.0,"2022-09-20 05:49:02",71,"t2_8f3682f1","author 1","url 1","2022-09-20 05:49:01"),
            ("author 2","title 2","name 2",102.0,"2022-09-20 05:49:02",72,"t2_8f3682f2","author 2","url 2","2022-09-20 05:49:02"),
            ("author 3","title 3","name 3",103.0,"2022-09-20 05:49:03",73,"t2_8f3682f3","author 3","url 3","2022-09-20 05:49:03")
        ]
        previous_new_posts_data = [
            ("author 2","title 2","name 2",82.0,"2022-09-20 05:49:02",62,"t2_8f3682f2","author 2","url 2","2022-09-20 05:49:02"),
            ("author 3","title 3","name 3",83.0,"2022-09-20 05:49:03",63,"t2_8f3682f3","author 3","url 3","2022-09-20 05:49:03"),
        ]
  
        processor = RedditProcessor() 
        processor.df_new_posts = dt.Frame(lastest_new_posts_data, names=POST_COLUMNS) 
