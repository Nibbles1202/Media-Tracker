from storage import load_items, save_items
from tracker import (
    add_items,
    view_items,
    update_status,
    delete_item,
    search_items,
    show_insights
)


def main():
    items = load_items()
    
    while True:
        print("=== Media Tracker ===")
        print("1. Add items")
        print("2. View items")
        print("3. Update status")
        print("4. Show insights")
        print("5. Delete item")
        print("6. Search items")
        print("7. Exit")

        choice = input("Choose: ")

        if choice == "1":
            add_items(items, save_items)
        elif choice == "2":
            view_items(items)
        elif choice == "3":
            update_status(items, save_items)
        elif choice == "4":
            show_insights(items)
        elif choice == "5":
            delete_item(items, save_items)
        elif choice == "6":
            search_items(items)
        elif choice == "7":
            break
        else:
            print("Invalid choice.\n")

if __name__ == "__main__":
    main()