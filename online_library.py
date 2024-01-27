library_catalog = {
    1: {
        "title": "Harry Potter",
        "author": "J.K. Rowling",
        "available_copies": 5,
        "total_copies": 5
    },
    2: {
        "title": "The God of Small Things",
        "author": "Arundhati Roy",
        "available_copies": 3,
        "total_copies": 3
    },
    3: {
        "title": "A Suitable Boy",
        "author": "Vikram Seth",
        "available_copies": 7,
        "total_copies": 7
    },
    4: {
        "title": "The Guide",
        "author": "R.K. Narayan",
        "available_copies": 4,
        "total_copies": 4
    },
    5: {
        "title": "Train to Pakistan",
        "author": "Khushwant Singh",
        "available_copies": 6,
        "total_copies": 6
    },
    6: {
        "title": "The Discovery of India",
        "author": "Jawaharlal Nehru",
        "available_copies": 2,
        "total_copies": 2
    }
}


def display_catalog():
    print("Library Catalog:")
    for title_id, details in library_catalog.items():
        print(f"\nTitle ID: {title_id}")
        print(f"  Title: {details['title']}")
        print(f"  Author: {details['author']}")
        print(f"  Available Copies: {details['available_copies']}")
        print(f"  Total Copies: {details['total_copies']}")


def borrow_book():
    title_id = int(input("Enter the Title ID of the book you want to borrow: "))

    if title_id in library_catalog:
        if library_catalog[title_id]["available_copies"] > 0:
            library_catalog[title_id]["available_copies"] -= 1
            print(f"Successfully borrowed '{library_catalog[title_id]['title']}'.")
        else:
            print("Sorry, the book is currently not available.")
    else:
        print("Book not found in the library catalog.")


def return_book():
    title_id = int(input("Enter the Title ID of the book you want to return: "))

    if title_id in library_catalog:
        if library_catalog[title_id]["available_copies"] < library_catalog[title_id]["total_copies"]:
            library_catalog[title_id]["available_copies"] += 1
            print(f"Successfully returned '{library_catalog[title_id]['title']}'.")
        else:
            print("You can't return more copies than the total available.")
    else:
        print("Book not found in the library catalog.")


while True:
    print("\nOptions:")
    print("1. Display Catalog")
    print("2. Borrow a Book")
    print("3. Return a Book")
    print("4. Quit")
    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        display_catalog()
    elif choice == "2":
        borrow_book()
    elif choice == "3":
        return_book()
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 4.")
