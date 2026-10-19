from langchain.agents import create_agent
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from tools import web_search, scrape_url
from dotenv import load_dotenv
load_dotenv()

llm = ChatGoogleGenerativeAI(
        model = 'gemini-2.5-flash-lite',
         max_tokens=70
    )

# creating the agents 
# Search Agent
def build_search_agent():
    return create_agent(
        tools=[web_search],
        model=llm
    )
 
# Reader Agent
def build_reader_agent():
    return create_agent(
        tools= [scrape_url],
        model=llm
    )
    
