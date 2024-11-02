import requests
from bs4 import BeautifulSoup
import logging
from typing import Dict, List, Tuple, Optional

def get_page_content(url: str) -> Optional[BeautifulSoup]:
    """Fetch and parse webpage content."""
    try:
        response = requests.get(url)
        response.raise_for_status()
        return BeautifulSoup(response.content, 'html.parser')
    except Exception as e:
        logger.error(f"Error fetching URL {url}: {str(e)}")
        return None

# Base configuration
BASE_URL = "https://wisconsinsupperclubs.com"
REGIONS = {
    "southeast": "/southeast-region/"
}

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('scraper.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

soup = get_page_content("https://wisconsinsupperclubs.com/southeast-region/")
if soup:
    # 使用 BeautifulSoup 物件處理網頁內容
    title = soup.find('title').text
    print(f"頁面標題: {title}")
else:
    print("無法獲取網頁內容")