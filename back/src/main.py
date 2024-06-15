from dotenv import load_dotenv
from pathlib import Path
import os

from business_info.yelp import YelpHandler

__version__ = '0.1.0'

# Goes back to root directory ".."
ROOT_DIR: str = Path(__file__).resolve(strict=True).parent.parent

# Load environment variables from .env file if it exists
load_dotenv(f"{ROOT_DIR}/.env")
yelp_api_key: str = os.getenv('YELP_API_KEY')

def main() -> None:
    yelp = YelpHandler(yelp_api_key)
    print(yelp.call_api("Sweden") \
              .deserialize_json() \
              .get_businesses())

if __name__ == '__main__':
    main()
