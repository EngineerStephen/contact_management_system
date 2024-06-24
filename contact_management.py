
#numbered menu
menu = ["Add a new contact", "Edit and existing contact", "Delete a contact", "Search for a Contact",
        "Display all contacts", "Export contacts to a text file", "Import contacts from a text file", "Quit"]
numbered_menu = [(index + 1, task) for index, task in (enumerate(menu))]

#welcome message
print()
print("Welcome to LDIA. Your #1 CLI app to manage your contacts. My name is Jimmy, your virtual assistant😀 ")
user_name = (input("Please tell me your name: ")).capitalize()
print()

#displaying menu options 
for number, task in numbered_menu:
    print (number, task)
print()

# taking user input   
while True:
    
    try:
        user_choice = int(input(f"{user_name}, What would you like to do? Please make a choice from the options above and enter the associated number:  "))
        if 1 <= user_choice <= (len(numbered_menu)):
            print(f"Okay you have chosen to {numbered_menu[user_choice - 1][1]}")
            print()
            
            user_addname = input("Please enter the name of the contact you would like to add in the format 'First Name Last Name':     ")
            user_addnumber = input(f"Please enter {user_addname}'s contact in the format 123-456-7890:  ")
            print(f"Contact {user_addname} with phone number {user_addnumber} has been added to your contact list")
            
        #if user chooses to add contact
            if user_choice == 1:

                def new_contacts(user_addname, user_addnumber):
                    contacts = {}
                    contact = {user_addname : user_addnumber}
                    contacts.update(contact)
                    return contacts
                new_contact = new_contacts(user_addname, user_addnumber)
                print(new_contact)
        #choosing to edit a contact 

        else:
            print("Please choose a valid option")
            print()
    except ValueError: 
        print("Invalid input. Please enter a number from the list")
        print()
    break







    



