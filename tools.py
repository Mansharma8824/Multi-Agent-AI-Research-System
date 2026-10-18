from langchain.tools import tool
import requests
from bs4 import BeautifulSoup
from tavily import TavilyClient
import os
from dotenv import load_dotenv
load_dotenv()
from rich import print

tavily = TavilyClient(api_key=os.getenv("TAVILIY_API_KEY"))

@tool
def web_search(query:str) -> str:
    """Search the web for recent and reliable information on a topic.Return Tittle, URLs, and snippets."""
    tavily_resuilt = tavily.search(query=query, max_results = 5)
    
    news_list = []
    for r in tavily_resuilt['results']:
        news_list.append(
            f"Tittle : {r['title']}\nURL : {r['url']}\nSnippet: {r['content'][:300]}\n"
        )
        
    return "\n===========\n".join(news_list)

print(web_search.invoke("what is heppening in france?"))
