# tools.py
import datetime
from langchain_core.tools import tool
from langchain_tavily import TavilySearch

@tool
def get_current_time(format: str = "%Y-%m-%d %H:%M:%S") -> str:
    """
    Returns the current date and time in the specified format.
    The docstring here is crucial, as it's the description the LLM sees.
    """
    now = datetime.datetime.now()
    return f"{now.strftime('%Y-%m-%d %H:%M:%S')} (EST Timezone) This is the current time in Toronto Timezone."

# Initialize the search tool
search_tool = TavilySearch(max_results=2)

# Create the new list of tools
tools = [get_current_time, search_tool]

# Create the dictionary to look up tools by their name
tools_by_name = {tool.name: tool for tool in tools}