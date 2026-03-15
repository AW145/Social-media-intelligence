import json

with open("updates.json") as f:
    updates = json.load(f)

updates = sorted(updates, key=lambda x: x["score"], reverse=True)

print("INSTAGRAM WEEKLY INTELLIGENCE\n")

for u in updates[:10]:
    print(u["score"], "-", u["title"])
    print(u["link"])
    print()
