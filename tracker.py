import json

def add_items(items, save_items):
    title = input("Title: ")
    category = input("Category (game/movie/show): ")
    status = "Not Started"

    rating_input = input("Rating (1-10, optional): ").strip()

    rating = rating_input if rating_input != "" else "N/A"

    items.append({
        "title": title,
        "category": category,
        "status": status,
        "rating": rating if rating else "N/A"
    })

    save_items(items)
    print("Item added.\n")


def view_items(items):
    if not items:
        print("No items yet.\n")
        return

    for i, item in enumerate(items, start=1):
        print(
            f"{i}. {item['title']} "
            f"[{item['category']}] - "
            f"{item['status']} - "
            f"Rating: {item.get('rating', 'N/A')}"
        )

        print()


def update_status(items, save_items):
    view_items(items)

    if not items:
        return

    try: 
        choice = int(input("Select item: "))

        if 1 <= choice <= len(items):
            print("1. Not Started")
            print("2. In Progress")
            print("3. Completed")

            status = input("Choose status: ")

            if status == "1":
                items[choice-1]["status"] = "Not Started"
            elif status == "2":
                items[choice-1]["status"] = "In Progress"
            elif status == "3":
                items[choice-1]["status"] = "Completed"

            save_items(items)
            print("Updated.\n")

    except ValueError:
        print("Invalid input.\n")
              
         
def load_items():
    try:
        with open("data.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_items(items):
    with open("data.json", "w") as file:
        json.dump(items, file, indent=4)

def delete_item(items, save_items):
    view_items(items)

    if not items:
        return
    
    try:
        choice = int(input("Enter item number to delete: "))

        if 1 <= choice <= len(items):
            removed = items.pop(choice - 1)
            save_items(items)
            print(f"Deleted: {removed['title']}\n")
        else:
            print("Invalid selection.\n")

    except ValueError:
        print("Please enter a valid number.\n")

def search_items(items):
    query = input("Search title: ").lower()

    results = [
        item for item in items
        if query in item["title"].lower()
    ]

    if not results:
        print("No matches found.\n")
        return
    
    print("\n=== SEARCH RESULTS ===")
    for i, item in enumerate(results, start=1):
        print(
            f"{i}. {item['title']} "
            f"[{item['category']}] - "
            f"{item['status']} - "
            f"Rating: {item.get('rating', 'N/A')}"
        )
        print()

def show_insights(items):
    if not items:
        print("No data yet.")
        return
    
    completed = [i for i in items if i["status"] == "Completed"]
    in_progress = [i for i in items if i["status"] == "In Progress"]

    rated_items = [i for i in items if i["rating"] != "N/A"]

    avg_rating = 0
    if rated_items:
        avg_rating = sum(float(i["rating"]) for i in rated_items) / len(rated_items)

    print("\n=== INSIGHTS ===")
    print(f"Total items: {len(items)}")
    print(f"Completed: {len(completed)}")
    print(f"In Progress: {len(in_progress)}")
    print(f"Average Rating: {avg_rating:.2f}\n")
    print()