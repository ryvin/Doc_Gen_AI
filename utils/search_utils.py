# utils/search_utils.py

import os
import logging
from serpapi import GoogleSearch
from dotenv import load_dotenv

logger = logging.getLogger(__name__)
load_dotenv()

SERPAPI_API_KEY = os.getenv('SERPAPI_API_KEY')

if not SERPAPI_API_KEY:
    logger.error("SERPAPI_API_KEY not found in .env file.")
    raise ValueError("SERPAPI_API_KEY not found in .env file.")

def perform_web_search(query: str) -> str:
    """Performs a web search using SerpApi and returns summarized results.

    Args:
        query: The search query string.

    Returns:
        A string summarizing the top search results.
    """
    logger.info("Performing web search for query: %s", query)
    params = {
        "engine": "google",
        "q": query,
        "api_key": SERPAPI_API_KEY,
        "num": 5,  # Number of results to retrieve
    }
    try:
        search = GoogleSearch(params)
        results = search.get_dict()
        organic_results = results.get("organic_results", [])
        summaries = []
        for result in organic_results:
            title = result.get("title", "")
            snippet = result.get("snippet", "")
            summaries.append(f"{title}\n{snippet}\n")
        return "\n".join(summaries)
    except Exception as e:
        logger.error("Error during web search: %s", e)
        return "No results found due to an error."
