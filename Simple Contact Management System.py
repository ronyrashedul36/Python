# --- Simple Contact Management System ---

contacts = {}

print("--- Add New Contacts ---")

name1 = input("Enter name for Contact1: ")

phone1 = input("Enter phone number for Contact 1: ")

contacts[name1] = phone1

name2 = input("Enter name for Contact 2: ")

phone2 = input("Enter phone number for Contact 2: ")

contacts[name2] = phone2

print("\n--- All Contacts Saved ---")
print(contacts)

print("\n--- Look up a Contact ---")

search_name = input("Whose phone number do you want to find? ")

phone_number = contacts.get(search_name)

if phone_number:
    print(f"The phone number for {search_name} is: {phone_number}")
else:
    print(f"Sorry, {search_name} is not in your contacts. ")