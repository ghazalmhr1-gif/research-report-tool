# Research Report Tool

Turns a topic into a structured research findings report in markdown, using the Serper (Google Search) API.

## Why I built this
Practicing quick research-to-report automation relevant to marketing and analyst roles — pulling live search results and turning them into a shareable, structured summary.

## How to run it
1. Get a free API key at [serper.dev](https://serper.dev)
2. Create a `.env` file with `SERPER_API_KEY=your_key_here`
3. Install dependencies: `pip install requests python-dotenv`
4. Run: `python research_report.py`
5. Enter a topic when prompted — a markdown report is saved to the project folder
## Why I built this
Built to practice the kind of research-to-report workflow a Go-To-Market analyst relies on — pulling live competitive and market signals via API instead of manual searching, and turning them into a structured, shareable summary in seconds.