import requests
from bs4 import BeautifulSoup
import os
from dotenv import load_dotenv

load_dotenv()
SERPAPI_KEY = os.getenv("SERPAPI_KEY")

def search_papers(query):
    # First try SerpApi
    try:
        serp_url = "https://serpapi.com/search"
        params = {
            "q": query,
            "engine": "google_scholar",
            "api_key": SERPAPI_KEY
        }
        response = requests.get(serp_url, params=params)
        response.raise_for_status()
        json_data = response.json()
        results = []
        if "organic_results" in json_data:
            for item in json_data["organic_results"]:
                results.append({
                    "title": item.get("title"),
                    "link": item.get("link"),
                    "snippet": item.get("snippet", "")
                })
        if results:
            return results
    except Exception as e:
        print("SerpApi failed:", e)

    # Fallback to ArXiv scraping
    try:
        print("Falling back to ArXiv...")
        query_url = f"https://arxiv.org/search/?query={query.replace(' ', '+')}&searchtype=all"
        html = requests.get(query_url).text
        soup = BeautifulSoup(html, "html.parser")
        results = []
        for item in soup.select(".arxiv-result"):
            title = item.select_one(".title").text.strip()
            link = item.select_one("p.list-title a")["href"]
            snippet = item.select_one(".abstract").text.replace("Abstract:", "").strip()
            results.append({
                "title": title,
                "link": link,
                "snippet": snippet
            })
            if len(results) >= 5:  # Limit to 5 results for demo
                break
        return results
    except Exception as e:
        print("ArXiv fallback also failed:", e)
        return "Unable to retrieve results from either SerpApi or ArXiv."

def extract_papers(json_data):
    results = []
    if json_data and "organic_results" in json_data:
        for item in json_data["organic_results"]:
            title = item.get("title")
            link = item.get("link")
            snippet = item.get("snippet", "")
            results.append({"title": title, "link": link, "snippet": snippet})
    return results
