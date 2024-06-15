from dotenv import load_dotenv
from pathlib import Path
import os

from business_info.yelp import YelpHandler

__version__ = '0.1.0'

# Goes back to root directory ".."
ROOT_DIR = Path(__file__).resolve(strict=True).parent.parent

# Load environment variables from .env file if it exists
load_dotenv(f"{ROOT_DIR}/.env")
yelp_api_key = os.getenv('YELP_API_KEY')
yelp = YelpHandler(yelp_api_key)

print(yelp.call_api("Sweden"))
