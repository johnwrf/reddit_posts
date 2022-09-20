from datatable import dt, fread
import csv
import logging
import traceback

logger = logging.getLogger(__name__)


def load_posts(listing, columns, base_path="./data"):
    """loads posts previously saved for the specified listing and returns as a datatable Frame."""
    try:
        path = f"{base_path}/{listing}.csv"
        logger.debug(f"loading {listing} posts from {path}")
        frame = fread(path)
    except dt.exceptions.IOError:
        logger.error(f'IOError when loading posts for {listing}')
        frame = dt.Frame([], names=columns)        
    except:
        logger.error(f'Exception when loading posts for {listing}')
        traceback.print_exc()
        frame = dt.Frame([], names=columns)        
    finally:
        return frame

    
def save_posts(listing, posts, base_path="./data"):
    """saves listing posts (datatable Frame) to disk"""
    try:
        path = f"{base_path}/{listing}.csv"
        logger.debug(f"saving {listing} posts to {path}")
        posts.to_csv(path=path, quoting=csv.QUOTE_NONNUMERIC)
        return True
    except dt.exceptions.IOError:
        logger.error(f'IOError when saving posts for {listing}')
        traceback.print_exc()
        raise
    except:
        logger.error(f'Exception when loading posts for {listing}')
        traceback.print_exc()
        raise
