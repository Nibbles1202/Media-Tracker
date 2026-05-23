import json

def add_items(items):
    title = input("Title: ")
    category = input("Category (game/movie/show): ")
    status = "Not Started"

    items.append({
        "title": title,
        "category": category,
        "status": status 
    })

    save_items(items)
    print("Item added.\n")


def view_items(items):
    if not items:
        print("No items yet.\n")
        return

    for i, item in enumerate(items, start=1):
        print(f"{i}. {item['title']} [{item['category']}] - {item['status']}")

        print()

def mark_complete(items):
    view_items(items)

    if not items:
        return

    try:
        choice = int(input("Enter number to mark complete: "))
        if 1 <= choice <= len(items):
            items[choice - 1]["status"] = "Completed"
            save_items(items)
            print("Marked as completed.\n")
        else:
            print("Invalid selection.\n")
    except ValueError:
        print("Please enter a number.\n")
        
def load_items():
    try:
        with open("data.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_items(items):
    with open("data.json", "w") as file:
        json.dump(items, file, indent=4)

def main():
    items = load_items()
    
    while True:
        print("=== Media Tracker ===")
        print("1. Add item")
        print("2. View items")
        print("3. Mark complete")
        print("4. Exit")

        choice = input("Choose: ")

        if choice == "1":
            add_items(items)
        elif choice == "2":
            view_items(items)
        elif choice == "3":
            mark_complete(items)
        elif choice == "4":
            break
        else:
            print("Invalid choice.\n")

if __name__ == "__main__":
    main()