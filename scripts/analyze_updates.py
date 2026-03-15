import json

with open("updates.json") as f:
    updates = json.load(f)

results = []

for item in updates:
    text = item["title"] + " " + item["summary"]

    score = 1

    if "algorithm" in text.lower():
        score = 5
    elif "reels" in text.lower():
        score = 4
    elif "creator" in text.lower():
        score = 3

    results.append({
        "title": item["title"],
        "link": item["link"],
        "score": score
    })

with open("updates.json","w") as f:
    json.dump(results,f)
