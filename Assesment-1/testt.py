def display_menu():
    print("\nWelcome to the E-Note Book Console Application")
    print("1. Add a Note")
    print("2. View Notes")
    print("3. Exit")

def add_note():
    title = input("Enter the title of the note: ")
    content = input("Enter the content of the note: ")
    with open(f"{title}.txt", "w") as note_file:
        note_file.write(content)
    print(f"Note titled '{title}' has been added successfully.")

def view_notes():
    note_name = input("\nEnter the title of the note you want to view : ")
    try:
        with open(f"{note_name}.txt", "r") as note_file:
            content = note_file.read()
        print(f"\nContent of '{note_name}':\n{content}")
    except FileNotFoundError:
        print(f"No note found with the title '{note_name}'.")

while True:
    display_menu()
    choice = input("\nEnter your choice (1-3): ")
    if choice == "1":
        add_note()
    elif choice == "2":
        view_notes()
    elif choice == "3":
        print("Exiting the application. Goodbye!")
        break
    else:
        print("Invalid choice, please choose a valid option (1-3).")

#test comment dhcioeoifef