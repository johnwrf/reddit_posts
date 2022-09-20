import datetime
import json
import requests
import logging
import traceback

logger = logging.getLogger(__name__)

def format_params(limit=None, timeframe=None):
    params = {}
    params["limit"] = limit if limit else ()
    params["t"] = timeframe if timeframe else ()
    return params

def datetime_parser(json_dict):
    for key, value in json_dict.items():
        
        if key in ["score","likes","view_count"]:
            json_dict[key] = value if value else 0
            
        if key in ["created","created_utc"]:
            try:
                json_dict[key] = datetime.datetime.utcfromtimestamp(value)
            except:
                pass
    return json_dict

def get_posts(listing, limit=None, timeframe=None, subreddit=None):
    """retrieves json for specified listing with optional limit and timeframe params under the optional subreddit

    limit = 100 or less
    timeframe = hour, day, week, month, year, all
    listing = controversial, best, hot, new, random, rising, top
    subreddit = 'python' or another subreddit
    """
    
    try:
        subr = f"r/{subreddit}/" if subreddit else ""
        params = format_params(limit=limit, timeframe=timeframe)
        request_url = f'https://www.reddit.com/{subr}{listing}.json'
        response = requests.get(request_url, params=params, headers={'User-agent': 'reddit_posts'})
        # response = response.json()
        response = json.loads(response.text, object_hook=datetime_parser)
    except:
        logger.error('An Error Occured')
        traceback.print_exc()
    return response
