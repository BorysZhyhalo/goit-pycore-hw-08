from typing import Callable, Dict, List, Tuple
from bot.commands import add_contact, change_contact, show_phone, show_all
from bot.commands import add_birthday, show_birthday, birthdays
from bot.commands import add_email, add_address
from bot.addressbook import AddressBook
from bot.notebook import Notebook
from bot.storage import save_data, load_data, save_notebook, load_notebook


def parse_input(user_input: str) -> Tuple[str, List[str]]:
    """Split user input into command and arguments."""
    cmd, *args = user_input.split()
    return cmd.strip().lower(), args

def main() -> None:
    """Run the CLI assistant bot."""
    book = load_data()
    notebook = load_notebook()

    contact_commands: Dict[str, Callable] = {
        "add": add_contact,
        "change": change_contact,
        "phone": show_phone,
        "all": show_all,
        "add-birthday": add_birthday,
        "show-birthday": show_birthday,
        "birthdays": birthdays,
        "add-email": add_email,
        "add-address": add_address,
    }

    note_commands: Dict[str, Callable] = {
    }

    print("Welcome to the assistant bot!")

    while True:
        user_input = input("Enter a command: ")
        if not user_input.strip():
            continue
        command, args = parse_input(user_input)

        if command in {"close", "exit"}:
            save_data(book)
            save_notebook(notebook)
            print("Good bye!")
            break

        if command == "hello":
            print("How can I help you?")
            continue

        if command in contact_commands:
            print(contact_commands[command](args, book))
        elif command in note_commands:
            print(note_commands[command](args, notebook))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
