from typing import List
from bot.errors import input_error
from bot.addressbook import AddressBook, Record

@input_error
def add_contact(args: List[str], book: AddressBook) -> str:
    if len(args) < 2:
        raise IndexError
    name, phone, *_ = args
    record = book.find(name)
    message = "Contact updated."
    
    if record is None:
        record = Record(name)
        book.add_record(record)
        message = "Contact added."

    record.add_phone(phone)
    return message

@input_error
def change_contact(args: List[str], book: AddressBook) -> str:
    name, old_phone, new_phone = args[0], args[1], args[2]

    record = book.find(name)
    if record is None:
        return "Contact not found."

    # знайти телефон для заміни
    for i, phone_obj in enumerate(record.phones):
        if phone_obj.value == old_phone:
            record.phones[i] = type(phone_obj)(new_phone)  # створює новий Phone (з валідацією)
            return "Contact updated."

    return "Old phone not found."

# Returns all phones for a contact in one line separated by "; "
@input_error
def show_phone(args: List[str], book: AddressBook) -> str:
    name = args[0]
    record = book.find(name)
    if record is None:
        return "Contact not found."

    phones = "; ".join(phone.value for phone in record.phones)
    return phones if phones else "No phones."

@input_error
def show_all(args: List[str], book: AddressBook) -> str:
    if not book.data:
        return "No contacts found."
    return "\n".join(str(record) for record in book.data.values())

@input_error
# Adds birthday to an existing contact; date must be in DD.MM.YYYY.
def add_birthday(args: List[str], book: AddressBook) -> str:
    name, bday = args[0], args[1]
    record = book.find(name)
    if record is None:
        return "Contact not found."

    record.add_birthday(bday)
    return "Birthday added."

@input_error
def show_birthday(args: List[str], book: AddressBook) -> str:
    name = args[0]
    record = book.find(name)
    if record is None:
        return "Contact not found."

    if record.birthday is None:
        return "Birthday not set."

    return record.birthday.value.strftime("%d.%m.%Y")

@input_error
# Prints upcoming birthdays for the next week using AddressBook.get_upcoming_birthdays().
def birthdays(args: List[str], book: AddressBook) -> str:
    upcoming = book.get_upcoming_birthdays()
    if not upcoming:
        return "No birthdays in the next 7 days."

    lines = [f"{u['name']}: {u['congratulation_date']}" for u in upcoming]
    return "\n".join(lines)

@input_error
def add_email(args: List[str], book: AddressBook) -> str:
    name, email = args[0], args[1]
    record = book.find(name)
    if record is None:
        return "Contact not found."
    record.add_email(email)
    return "Email added."

@input_error
def add_address(args: List[str], book: AddressBook) -> str:
    name = args[0]
    address = " ".join(args[1:])
    record = book.find(name)
    if record is None:
        return "Contact not found."
    record.add_address(address)
    return "Address added."
