from langchain_community.tools import WikipediaQueryRun, DuckDuckGoSearchRun
from langchain_community.utilities import WikipediaAPIWrapper
from langchain.tools import Tool
from datetime import datetime

def save_to_txt_file(data: str, filename: str = "research_output.txt"):
    timestamp = datetime.now().strftime("%Y%m%d_%H:%M:%S")
    formatted_text = f"--- Research Output ---\nTimestamp: {timestamp} ---\n\n{data}\n\n"

    with open(filename, "a", encoding="utf-8") as file:
        file.write(formatted_text)

    return f"Data saved to {filename}"

save_tool = Tool(
    name="save_to_txt_file",
    func=save_to_txt_file,
    description="Saves the provided text data to a local text file with a timestamp. Input should be the text data to save.",
)


search = DuckDuckGoSearchRun()
search_tool = Tool(
    name="search",
    func=search.run,
    description="Search the web. Useful for when you need to look up current events or find information that is not in your training data. Input should be a search query.",
)

api_wrapper = WikipediaAPIWrapper(top_k_results=2, doc_content_chars_max=200)
wiki_tool = WikipediaQueryRun(api_wrapper=api_wrapper)