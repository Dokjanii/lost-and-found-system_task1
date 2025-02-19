import json
import utils

def load_data():
    try:
        with open("data.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_data(items):
    with open("data.json", "w") as file:
        json.dump(items, file, indent=4)

def report_item():
    items = load_data()
    item = utils.get_item_details()
    item["id"] = len(items) + 1
    items.append(item)
    save_data(items)
    print("Item reported successfully!")

def search_item():
    items = load_data()
    query = input("Enter item name or category: ")
    results = utils.search_items(items, query)
    utils.display_results(results)

def claim_item():
    items = load_data()
    item_id = int(input("Enter item ID to claim: "))
    for item in items:
        if item["id"] == item_id and not item["claimed"]:
            item["claimed"] = True
            save_data(items)
            print("Item successfully claimed!")
            return
    print("Item not found or already claimed.")

def menu():
    while True:
        print("1. Report a Found Item")
        print("2. Search for a Lost Item")
        print("3. View All Unclaimed Items")
        print("4. Claim an Item")
        print("5. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            report_item()
        elif choice == "2":
            search_item()
        elif choice == "3":
            utils.display_results([item for item in load_data() if not item["claimed"]])
        elif choice == "4":
            claim_item()
        elif choice == "5":
            break

if __name__ == "__main__":
    menu()
