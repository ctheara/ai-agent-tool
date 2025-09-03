# ai-agent-tool

An AI agent that uses web search, Wikipedia, file saving, and dad joke tools. Built with LangChain and OpenAI.

## Features

- Web search (DuckDuckGo)
- Wikipedia lookup
- Save research output to a timestamped text file
- Fetch a random dad joke from the internet

## Setup (Windows)

1. **Create and activate a virtual environment:**

   ```powershell
   python -m venv venv
   .\venv\Scripts\activate
   ```

2. **Install dependencies:**

   ```powershell
   pip install -r requirements.txt
   ```

3. **Set up environment variables:**
   - Create a `.env` file with your OpenAI API key:
     ```
     OPENAI_API_KEY=your-key-here
     ```

## Usage

Run the agent:

```powershell
python main.py
```

You will be prompted for a research query. If you want a dad joke, include "dad joke" in your request.

## Tools

- **search**: Web search for current information
- **wiki_tool**: Wikipedia lookup
- **save_to_txt_file**: Save output to `research_output.txt`
- **get_dad_joke**: Fetch a random dad joke

## Output

Results are structured with topic, summary, sources, tools used, and (optionally) a dad joke.
