import os
import sys
import json


# Toont alle contacten op het scherm.
def display(addressbook: list):
    if not addressbook:
        print("\nThe addressbook is empty.")
        return

    for index, contact in enumerate(addressbook, start=1):
        print("======================================")
        print(f"Position: {index}")
        print(f"First name: {contact['first_name']}")
        print(f"Last name: {contact['last_name']}")

        emails_str = ", ".join(contact['emails'])
        phones_str = ", ".join(contact['phone_numbers'])

        print(f"Emails: {emails_str}")
        print(f"Phone numbers: {phones_str}")


# Sorteert de contacten op voornaam van A naar Z.
def list_contacts(addressbook: list):
    return sorted(addressbook, key=lambda x: x['first_name'])


# Voegt een nieuw contact toe aan het adresboek.
def add_contact(addressbook: list):
    print()
    fname = input("Firstname: ")
    lname = input("Lastname: ")

    if not fname.isalpha() or not lname.isalpha():
        print("Error: Names must only contain letters.")
        return

    email_raw = input("Emails: ").split(',')
    emails = []
    for e in email_raw:
        clean_e = e.strip()
        if '@' in clean_e and clean_e not in emails:
            emails.append(clean_e)

    phone_raw = input("Phonenumbers: ").split(',')
    phones = []
    for p in phone_raw:
        clean_p = p.strip()
        if clean_p and clean_p not in phones:
            phones.append(clean_p)

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


# Verwijdert een contact op basis van het ID-nummer.
def remove_contact(addressbook: list):
    try:
        print()
        target_id = int(input("Enter ID to remove: "))
        initial_length = len(addressbook)

        addressbook[:] = [c for c in addressbook if c['id'] != target_id]

        if len(addressbook) < initial_length:
            print(f"Contact {target_id} removed.")
        else:
            print("ID not found.")
    except ValueError:
        print("Invalid input. Please enter a numeric ID.")


# Voegt dubbele contacten met dezelfde naam samen.
def merge_contacts(addressbook: list):
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
            group.sort(key=lambda x: x['id'], reverse=True)
            main_contact = group[0]

            for i in range(1, len(group)):
                other = group[i]
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


# Leest de contacten in vanuit het JSON-bestand.
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


# Schrijft de contacten weg naar het JSON-bestand.
def write_to_json(filename, addressbook: list) -> None:
    json_object = json.dumps(addressbook, indent=4)
    with open(os.path.join(sys.path[0], filename), "w") as outfile:
        outfile.write(json_object)


# Start het hoofdmenu van het programma.
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