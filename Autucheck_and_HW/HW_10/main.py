from faker import Faker
from functools import wraps
from ab_classes import AddressBook, Phone, Name, Record, Field
import pickle


adress_book = AddressBook()


fake = Faker("uk-UA")
Faker.seed(1)


def faker_dict() -> dict:
    contacts_dict = dict()

    for i in range(10):
        contacts_dict[fake.name().lower()] = fake.phone_number()

    return contacts_dict


def show_help(user_input):
    return f'"hello"ex=hello (show welcome)\n"add"  example: add name phone_number(add name and phone number)\n"change" example: change name new_numder(change phone number)\n"phone" example:phone name (show phone number)\n"show_all" example: show_all(show all phone book)\n"del"  example: del name(del name and phone number)\n"good bye", "quit", "exit", "bye", "close"(close app)\n"help" example: help (show commands list)'


def decor_input_error(func):
    @wraps(func)
    def inner_func(*args, **kwargs):
        try:
            result = func(*args, **kwargs)

        except IndexError:
            print("Something wrong ")
            return main()
        except TypeError:
            print("Something wrong")
            return main()
        except KeyError:
            print("Something wrong")
            return main()
        except ValueError:
            print("Something wrong")
            return main()
        return result

    return inner_func


def log_decorator(func):
    @wraps(func)
    def inner(*args, **kwargs):
        result = func(*args, **kwargs)
        with open("phone_book.bin", "wb") as file:
            pickle.dump(adress_book, file)
        return result

    return inner


def del_contact(user_input: str) -> str:
    name = Name(user_input[1])
    rec: Record = adress_book.get(name.value)
    if rec:
        return adress_book.del_record(rec)
    return f"No contact {name} in address book"


def exit(user_input: str) -> None:
    return None


def hello_func(user_input: str) -> str:
    return "How can I help you?"


def phone(user_input: str) -> str:
    return adress_book[user_input[1]]


def show_all(user_input: str) -> dict:
    return adress_book


def add_name_and_phone_number(user_input: str) -> dict:
    name = Name(user_input[1])
    phone = Phone(user_input[2])
    rec: Record = adress_book.get(str(name))
    if rec:
        return rec.add_phone(phone)
    rec = Record(name, phone)

    return adress_book.add_record(rec)


def change(user_input: str) -> dict:
    name = Name(user_input[1])
    old_phone = Phone(user_input[2])
    new_phone = Phone(user_input[3])
    rec: Record = adress_book.get(str(name))
    if rec:
        return rec.change_phone(old_phone, new_phone)
    return f"No contact {name} in address book"


def del_phone(user_input: str) -> str:
    name = Name(user_input[1])
    phone = Phone(user_input[2])
    rec: Record = adress_book.get(str(name))
    if rec:
        return rec.del_phone(phone)
    return f"No contact {name} in address book"


@decor_input_error
def get_handler(command: str) -> object:
    for comm, func in COMMANDS.items():
        if command in comm:
            return func


@decor_input_error
def main():
    print('"help" show list of commands"')
    while True:
        user_input = input(">>>").lower()
        user_input = user_input.strip().split()
        return_func = get_handler(user_input[0])
        if return_func == exit:
            print("Good bye! Have a nice day!")
            break
        result = return_func(user_input)
        print(result)


COMMANDS = {
    ("good bye", "quit", "exit", "bye", "close"): exit,
    ("hello", "hey"): hello_func,
    ("додай", "add"): add_name_and_phone_number,
    ("change",): change,
    ("phone", "show_phone"): phone,
    ("show_all", "show_book"): show_all,
    ("del_contact", "remove_contact"): del_contact,
    ("del"): del_phone,
    ("help",): show_help,
}


if __name__ == "__main__":
    main()
