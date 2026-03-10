import pickle
from bot.addressbook import AddressBook
from bot.notebook import Notebook

def save_data(book: AddressBook, filename: str = "addressbook.pkl") -> None:
    """Save the address book to a file using pickle."""
    with open(filename, "wb") as file:
        pickle.dump(book, file)

def load_data(filename: str = "addressbook.pkl") -> AddressBook:
    """Load the address book from a file or return a new one if file does not exist."""
    try:
        with open(filename, "rb") as file:
            return pickle.load(file)
    except FileNotFoundError:
        return AddressBook()

def save_notebook(notebook: Notebook, filename: str = "notebook.pkl") -> None:
    """Save the notebook to a file using pickle."""
    with open(filename, "wb") as file:
        pickle.dump(notebook, file)

def load_notebook(filename: str = "notebook.pkl") -> Notebook:
    """Load the notebook from a file or return a new one if file does not exist."""
    try:
        with open(filename, "rb") as file:
            return pickle.load(file)
    except FileNotFoundError:
        return Notebook()