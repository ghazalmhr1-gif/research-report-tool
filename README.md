# Research Report Tool

Turns a topic into a structured research findings report in markdown, using the Serper (Google Search) API.

## Why I built this
Built to practice the kind of research-to-report workflow a Go-To-Market analyst relies on — pulling live competitive and market signals via API instead of manual searching, and turning them into a structured, shareable summary in seconds.

## How to run it
1. Get a free API key at [serper.dev](https://serper.dev)
2. Create a `.env` file with `SERPER_API_KEY=your_key_here`
3. Install dependencies: `pip install requests python-dotenv`
4. Run it interactively: `python research_report.py` (you'll be prompted for a topic)
   Or run it directly: `python research_report.py "your topic here" --num 5`
5. A markdown report is saved to the project folder