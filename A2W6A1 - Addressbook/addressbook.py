import os
import sys
import json

# --- 1. DISPLAY LOGIC ---
def display(addressbook: list):
    """Prints the contacts in the required format."""
    if not addressbook:
        print("\nThe addressbook is empty.")
        return

    for index, contact in enumerate(addressbook, start=1):
        print("======================================")
        print(f"Position: {index}")
        print(f"First name: {contact['first_name']}")
        print(f"Last name: {contact['last_name']}")
        
        # .join() takes a list and turns it into a string separated by commas
        emails_str = ", ".join(contact['emails'])
        phones_str = ", ".join(contact['phone_numbers'])
        
        print(f"Emails: {emails_str}")
        print(f"Phone numbers: {phones_str}")

# --- 2. SORTING LOGIC ---
def list_contacts(addressbook: list):
    """Returns a copy of the list sorted by First Name in Descending order."""
    # We use a lambda to tell Python to sort specifically by the 'first_name' key
    return sorted(addressbook, key=lambda x: x['first_name'].lower(), reverse=True)

# --- 3. ADD CONTACT LOGIC ---
def add_contact(addressbook: list):
    """Prompts user for input and adds a new contact dictionary."""
    fname = input("Firstname: ")
    lname = input("Lastname: ")
    
    # Validation: alphabetic only
    if not fname.isalpha() or not lname.isalpha():
        print("Error: Names must only contain letters.")
        return

    # Emails: split by comma, strip whitespace, and check for '@'
    email_raw = input("Emails: ").split(',')
    emails = []
    for e in email_raw:
        clean_e = e.strip()
        if '@' in clean_e and clean_e not in emails:
            emails.append(clean_e)
    
    # Phone Numbers: split by comma and strip whitespace
    phone_raw = input("Phonenumbers: ").split(',')
    phones = []
    for p in phone_raw:
        clean_p = p.strip()
        if clean_p and clean_p not in phones:
            phones.append(clean_p)

    # Generate ID: Find the current highest ID and add 1
    current_ids = [c['id'] for c in addressbook]
    new_id = max(current_ids) + 1 if current_ids else 1
    
    new_contact = {
        "id": new_id,
        "first_name": fname,
        "last_name": lname,
        "emails": emails,
        "phone_numbers": phones
    }
    
    addressbook.append(new_contact)
    print("Contact added to addressbook")

# --- 4. REMOVE LOGIC ---
def remove_contact(addressbook: list):
    """Removes a contact based on its ID."""
    try:
        target_id = int(input("Enter ID to remove: "))
        found = False
        
        for i in range(len(addressbook)):
            if addressbook[i]['id'] == target_id:
                addressbook.pop(i)
                print(f"Contact {target_id} removed.")
                found = True
                break
        
        if not found:
            print("ID not found.")
    except ValueError:
        print("Invalid input. Please enter a numeric ID.")

# --- 5. MERGE LOGIC ---
def merge_contacts(addressbook: list):
    """Merges contacts with the same full name into the record with the highest ID."""
    # Dict to keep track of: "firstname lastname" -> [list of contact objects]
    name_groups = {}
    
    for contact in addressbook:
        full_name = f"{contact['first_name']} {contact['last_name']}".lower()
        if full_name not in name_groups:
            name_groups[full_name] = []
        name_groups[full_name].append(contact)
    
    merged_list = []
    
    for name in name_groups:
        group = name_groups[name]
        if len(group) > 1:
            # Sort group so the highest ID is at index 0
            group.sort(key=lambda x: x['id'], reverse=True)
            main_contact = group[0]
            
            # Combine data from others into the main_contact
            for i in range(1, len(group)):
                other = group[i]
                # Add emails/phones only if they aren't already there
                for mail in other['emails']:
                    if mail not in main_contact['emails']:
                        main_contact['emails'].append(mail)
                for phone in other['phone_numbers']:
                    if phone not in main_contact['phone_numbers']:
                        main_contact['phone_numbers'].append(phone)
            
            merged_list.append(main_contact)
        else:
            merged_list.append(group[0])
            
    addressbook[:] = merged_list
    print("Merge complete.")

# --- 6. FILE I/O (DO NOT CHANGE) ---
def read_from_json(filename) -> list:
    addressbook = list()
    try:
        with open(os.path.join(sys.path[0], filename)) as outfile:
            json_data = json.load(outfile)
            for contact in json_data:
                addressbook.append(contact)
    except (FileNotFoundError, json.JSONDecodeError):
        return []
    return addressbook

def write_to_json(filename, addressbook: list) -> None:
    json_object = json.dumps(addressbook, indent = 4)
    with open(os.path.join(sys.path[0], filename), "w") as outfile:
        outfile.write(json_object)

# --- 7. MAIN MENU ---
def main(json_file):
    addressbook = read_from_json(json_file)

    while True:
        print("\n[L] List contacts")
        print("[A] Add contact")
        print("[R] Remove contact")
        print("[M] Merge contacts")
        print("[Q] Quit program")
        
        choice = input("Choice: ").strip().upper()

        if choice == 'L':
            sorted_addressbook = list_contacts(addressbook)
            display(sorted_addressbook)
        elif choice == 'A':
            add_contact(addressbook)
            write_to_json(json_file, addressbook)
        elif choice == 'R':
            remove_contact(addressbook)
            write_to_json(json_file, addressbook)
        elif choice == 'M':
            merge_contacts(addressbook)
            write_to_json(json_file, addressbook)
        elif choice == 'Q':
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main('contacts.json')