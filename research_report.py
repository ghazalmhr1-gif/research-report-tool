import os
import sys
import argparse
import requests
from datetime import date
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("SERPER_API_KEY")

def search(query, num_results=10):
    if not API_KEY:
        print("Error: SERPER_API_KEY not found. Check your .env file.")
        sys.exit(1)
    url = "https://google.serper.dev/search"
    headers = {"X-API-KEY": API_KEY, "Content-Type": "application/json"}
    payload = {"q": query, "num": num_results}
    try:
        response = requests.post(url, json=payload, headers=headers, timeout=10)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Error contacting Serper API: {e}")
        sys.exit(1)
    return response.json()

def build_report(query, data):
    lines = [f"# Research Report: {query}", f"*Generated {date.today()}*", ""]
    organic = data.get("organic", [])
    if not organic:
        lines.append("No results found.")
        return "\n".join(lines)
    lines.append("## Key Findings\n")
    for item in organic:
        title = item.get("title", "")
        snippet = item.get("snippet", "")
        link = item.get("link", "")
        lines.append(f"- **{title}** — {snippet} ([source]({link}))")
    return "\n".join(lines)

def safe_filename(topic):
    slug = "".join(c if c.isalnum() or c == " " else "" for c in topic)
    slug = slug.strip().replace(" ", "_").lower()[:40]
    return f"report_{slug or 'untitled'}.md"

def main():
    parser = argparse.ArgumentParser(description="Generate a markdown research report from a topic.")
    parser.add_argument("topic", nargs="?", help="Research topic (skip to be prompted)")
    parser.add_argument("--num", type=int, default=10, help="Number of results to include (default: 10)")
    args = parser.parse_args()

    topic = args.topic or input("Enter a research topic: ")
    data = search(topic, num_results=args.num)
    report = build_report(topic, data)
    filename = safe_filename(topic)
    with open(filename, "w") as f:
        f.write(report)
    print(f"Saved to {filename}")

if __name__ == "__main__":
    main()
