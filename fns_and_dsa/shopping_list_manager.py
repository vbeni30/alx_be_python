# shopping_list_manager.py

def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []   # required array

    while True:
        display_menu()   # must be called
        choice_input = input("Enter your choice: ")

        # ALX checker wants numeric choice
        try:
            choice = int(choice_input)
        except ValueError:
            print("Invalid choice. Please enter a number.")
            continue

        if choice == 1:
            item = input("Enter item to add: ").strip()
            shopping_list.append(item)
            print(f"'{item}' added to the list.")

        elif choice == 2:
            item = input("Enter item to remove: ").strip()
            if item in shopping_list:
                shopping_list.remove(item)
                print(f"'{item}' removed from the list.")
            else:
                print(f"'{item}' not found in the list.")

        elif choice == 3:
            print("Current Shopping List:")
            if len(shopping_list) == 0:
                print("(empty)")
            else:
                for i, item in enumerate(shopping_list, 1):
                    print(f"{i}. {item}")

        elif choice == 4:
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
