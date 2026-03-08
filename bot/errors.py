"""
Decorator to convert common input/runtime errors into user-friendly messages.
"""
def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)

        except IndexError:
            return "Not enough arguments."

        except ValueError as e:
            # show a specific reason (phone/date/name)
            return str(e) if str(e) else "Invalid value."

        except KeyError:
            return "Contact not found."

        except Exception:
            # Fallback for unexpected errors (prevents CLI crash)
            return "Unexpected error. Please try again."

    return inner