def display_menu():
    print("\nShopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []  # This is the array (list) you need
    while True:
        display_menu()  # Ensures display_menu is called
        try:
            choice = int(input("Enter your choice (1-4): "))  # Ensure choice is an integer
        except ValueError:
            print("Invalid input! Please enter a number between 1 and 4.")
            continue

        if choice == 1:
            # Prompt for and add an item
            item = input("Enter the item to add: ")
            shopping_list.append(item)
            print(f"{item} has been added to the shopping list.")
        
        elif choice == 2:
            # Prompt for and remove an item
            item = input("Enter the item to remove: ")
            if item in shopping_list:
                shopping_list.remove(item)
                print(f"{item} has been removed from the shopping list.")
            else:
                print(f"{item} is not in the shopping list.")
        
        elif choice == 3:
            # Display the shopping list
            if shopping_list:
                print("\nCurrent shopping list:")
                for i, item in enumerate(shopping_list, start=1):
                    print(f"{i}. {item}")
            else:
                print("The shopping list is empty.")
        
        elif choice == 4:
            print("Goodbye!")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

