# Reddit Posts

## Table of Contents
- [Reddit Posts](#reddit-posts)
  - [Table of Contents](#table-of-contents)
  - [Overview](#overview)
  - [Usage Instructions](#usage-instructions)
    - [Running the python application](#running-the-python-application)
      - [Python modules used](#python-modules-used)
    - [Running the jupyter notebook](#running-the-jupyter-notebook)
      - [Installation](#installation)
  - [Limitations](#limitations)
    - [Post fields that will be stored](#post-fields-that-will-be-stored)
  - [Reddit No Credentials API Reference](#reddit-no-credentials-api-reference)
      - [Reddit format](#reddit-format)
      - [Subreddit format](#subreddit-format)
    - [List of the Reddit’s JSON Keys](#list-of-the-reddits-json-keys)

## Overview
This applications uses Reddit's no credentials json API to retrieve posts from Reddit and compare the latest results from Reddit vs the results from the last program execution. Each time the program runs, the posts returned from Reddit are stored in a file so they can be loaded during during the subsequent program execution.

For each program execution, the following results are printed:
1. New posts from the last program execution
2. Posts that are no longer within the top 75 posts
3. Posts that had a vote count (score) change and by how much

## Usage Instructions

### Running the python application
You can run the application from the terminal as follows:
```
python3 src/main.py
```

#### Python modules used
requests
datatable
datetime
numpy
pandas

### Running the jupyter notebook
Run jupyter as follows
```
jupyter notebook
```

Then navigate to the notbook folder under `reddit_posts/notebooks`
and open `reddit_posts.ipynb`


#### Installation
To run the notebook you need to install Jupyter.  You can easily install jupyter directly via homebrew, or by installing anaconda, which also bundles jypiter
```
brew install jupyter
brew install --cask anaconda
```



## Limitations
1. This program uses Reddit's no credentials API, which do not support pagination and return a maximum of 100 results.  
2. Due to #1, the program only tracks the posts retrieved from the last execution, so each time the program is executed, the previous execution posts are replaced with the new ones that are retrieved from Reddit. 
3. The timeframe for all posts retrieved will be the last hour. See `timeframe` parameter below.  And a maximum of 100 posts will be retrieved for each Reddit API that is called.
4. Only a subset of fields are retrieved for each post (see #Post-fields-that-will-be-stored below). These are a minimal set of fields that are needed for the program to run and also include general data about each post.

### Post fields that will be stored
author_fullname
title
name
score
created
view_count
id
author
url
created_utc


## Reddit No Credentials API Reference

#### Reddit format
https://www.reddit.com/r/{listing}.json?limit={count}&t={timeframe}
listing = controversial, best, hot, new, popular, random, rising, top
timeframe = hour, day, week, month, year, all
count = maximum number of posts to retrieve. Limited at 100
For example
https://www.reddit.com/r/popular.json?limit=100
https://www.reddit.com/r/popular.json
https://www.reddit.com/new.json
https://www.reddit.com/top.json?limit=100


#### Subreddit format
https://www.reddit.com/r/{subreddit}/{listing}.json?limit={count}&t={timeframe}
listing = controversial, best, hot, new, random, rising, top
timeframe = hour, day, week, month, year, all
count = maximum number of posts to retrieve. Limited at 100
For example
https://www.reddit.com/r/python/new.json?limit=100&t=day
https://www.reddit.com/r/python/top.json?limit=100&t=day

### List of the Reddit’s JSON Keys
approved_at_utc
subreddit
selftext
author_fullname
saved
mod_reason_title
gilded
clicked
title
link_flair_richtext
subreddit_name_prefixed
hidden
pwls
link_flair_css_class
downs
thumbnail_height
top_awarded_type
hide_score
name
quarantine
link_flair_text_color
upvote_ratio
author_flair_background_color
subreddit_type
ups
total_awards_received
media_embed
thumbnail_width
author_flair_template_id
is_original_content
user_reports
secure_media
is_reddit_media_domain
is_meta
category
secure_media_embed
link_flair_text
can_mod_post
score
approved_by
author_premium
thumbnail
edited
author_flair_css_class
author_flair_richtext
gildings
content_categories
is_self
mod_note
created
link_flair_type
wls
removed_by_category
banned_by
author_flair_type
domain
allow_live_comments
selftext_html
likes
suggested_sort
banned_at_utc
view_count
archived
no_follow
is_crosspostable
pinned
over_18
all_awardings
awarders
media_only
link_flair_template_id
can_gild
spoiler
locked
author_flair_text
treatment_tags
visited
removed_by
num_reports
distinguished
subreddit_id
mod_reason_by
removal_reason
link_flair_background_color
id
is_robot_indexable
report_reasons
author
discussion_type
num_comments
send_replies
whitelist_status
contest_mode
mod_reports
author_patreon_flair
author_flair_text_color
permalink
parent_whitelist_status
stickied
url
subreddit_subscribers
created_utc
num_crossposts
media
is_video
