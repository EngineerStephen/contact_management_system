

menu = {"Add a new contact", "Edit and existing contact", "Delete a contact", "Search for a Contact",
        "Display all contacts", "Export contacts to a text file", "Import contacts from a text file", "Quit"}
numbered_menu = [(index + 1, task) for index, task in enumerate(menu)]

print()
print("Welcome to KNOW IT ALL. Your #1 CLI app to manage your contacts. My name is Jimmy, your virtual assistant")
print()
user_name = (input("Please tell me your name:   ")).capitalize()
print()
print()

for number, task in numbered_menu:
    print (number, task)
print()

while True:
    user_choice = int(input("What would you like to do?  "))
    if 1 <= user_choice <= (len(numbered_menu)):
        print(f"Okay you have chosen to {numbered_menu[user_choice - 1][1]}")
        print()
    else:
        print()
        print("Please choose a valid option")
        print()
        continue





