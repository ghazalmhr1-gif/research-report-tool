import os
import requests
from datetime import date
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("SERPER_API_KEY")

def search(query, num_results=10):
    url = "https://google.serper.dev/search"
    headers = {"X-API-KEY": API_KEY, "Content-Type": "application/json"}
    payload = {"q": query, "num": num_results}
    response = requests.post(url, json=payload, headers=headers)
    response.raise_for_status()
    return response.json()

def build_report(query, data):
    lines = [f"# Research Report: {query}", f"*Generated {date.today()}*", ""]
    organic = data.get("organic", [])
    lines.append("## Key Findings\n")
    for item in organic:
        title = item.get("title", "")
        snippet = item.get("snippet", "")
        link = item.get("link", "")
        lines.append(f"- **{title}** — {snippet} ([source]({link}))")
    return "\n".join(lines)

if __name__ == "__main__":
    topic = input("Enter a research topic: ")
    data = search(topic)
    report = build_report(topic, data)
    filename = f"report_{topic.replace(' ', '_')[:30]}.md"
    with open(filename, "w") as f:
        f.write(report)
    print(f"Saved to {filename}")
