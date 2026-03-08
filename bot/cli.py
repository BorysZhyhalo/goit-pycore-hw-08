from typing import Callable, Dict, List, Tuple
from bot.commands import add_contact, change_contact, show_phone, show_all
from bot.commands import add_birthday, show_birthday, birthdays
from bot.addressbook import AddressBook


def parse_input(user_input: str) -> Tuple[str, List[str]]:
    cmd, *args = user_input.split()
    return cmd.strip().lower(), args

def main() -> None:
    book: AddressBook = AddressBook()
    
    # Command router: maps CLI command names to handler functions.
    commands: Dict[str, Callable[[List[str], AddressBook], str]] = {
    "add": add_contact,
    "change": change_contact,
    "phone": show_phone,
    "all": show_all,
    "add-birthday": add_birthday,
    "show-birthday": show_birthday,
    "birthdays": birthdays
}

    print("Welcome to the assistant bot!")

    while True:
        user_input = input("Enter a command: ")
        if not user_input.strip():
            continue
        command, args = parse_input(user_input)

        if command in {"close", "exit"}:
            print("Good bye!")
            break

        if command == "hello":
            print("How can I help you?")
            continue

        handler = commands.get(command)

        if handler:
            result = handler(args, book)
            print(result)
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()


