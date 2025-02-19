import json

def get_item_details():
    name = input("Enter item name: ")
    category = input("Enter category: ")
    location = input("Enter location found: ")
    date_found = input("Enter date found (YYYY-MM-DD): ")
    return {"name": name, "category": category, "location": location, "date_found": date_found, "claimed": False}

def search_items(items, query):
    return [item for item in items if query.lower() in item["name"].lower() or query.lower() in item["category"].lower()]

def display_results(results):
    if not results:
        print("No items found.")
    for item in results:
        print(json.dumps(item, indent=4))
