from reddit_processor import RedditProcessor
import logging
import sys

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler("debug.log"),
        logging.StreamHandler(sys.stdout)
    ]
)
logger = logging.getLogger(__name__)

def run():
    processor = RedditProcessor()
    processor.get_new_posts()
    processor.get_not_top75_posts()
    processor.get_scores_changed_posts()


if __name__ == "__main__":
    run()