from faker import Faker
import json
from functools import wraps
from normalize import normalize


abort_list = ["good bye", "close", "exit"]

with open("phone_book.json", "r") as file:
    contacts = json.load(file)

fake = Faker("uk-UA")
Faker.seed(1)


def faker_dict() -> dict:
    contacts_dict = dict()

    for i in range(10):
        contacts_dict[normalize(fake.name()).lower()] = fake.phone_number()

    return contacts_dict


def show_help(user_input):
    return f'"hello"ex=hello (show welcome)\n"add"  example: add name phone_number(add name and phone number)\n"change" example: change name new_numder(change phone number)\n"phone" example:phone name (show phone number)\n"show_all" example: show_all(show all phone book)\n"del"  example: del name(del name and phone number)\n"help" example: help (show commands list)'


def decor_input_error(func):
    @wraps(func)
    def inner_func(*args, **kwargs):
        try:
            result = func(*args, **kwargs)

        except IndexError:
            print("Something wrong ")
            return main()
        except TypeError:
            print("Something wrong' ")
            return main()
        except KeyError:
            print("Something wrong ")
            return main()
        except ValueError:
            print("Something wrong ")
            return main()
        return result

    return inner_func


def log_decorator(func):
    @wraps(func)
    def inner(*args, **kwargs):
        result = func(*args, **kwargs)
        with open("phone_book.json", "w") as file:
            json.dump(contacts, file)
        return result

    return inner


@log_decorator
def del_contact(user_input: str) -> str:
    number = contacts.pop(user_input[1])

    return f"{user_input[1]} with number{number} has been del"


def hello_func(user_input: str) -> str:
    return "How can I help you?"


def phone(user_input: str) -> str:
    return contacts[user_input[1]]


def show_all(user_input: str) -> dict:
    return contacts


@log_decorator
def add_name_and_phone_number(user_input: str) -> dict:
    contacts[normalize(user_input[1])] = user_input[2]

    return f"contact {user_input[1].capitalize()} which has the number {user_input[2]} add to phone book"


@log_decorator
def change(user_input: str) -> dict:
    value = contacts.pop(user_input[1])
    contacts[normalize(user_input[1])] = user_input[2]

    return (
        f"{user_input[1].capitalize()}:{value} changed phone number to {user_input[2]}"
    )


@decor_input_error
def get_handler(command: str) -> object:
    return COMMANDS[command]


@decor_input_error
def main():
    print('"help" show list of commands"')
    while True:
        user_input = input(">>>").lower()
        if user_input in abort_list:
            print("Good bye! Have a nice day!")
            break
        user_input = user_input.strip().split()
        result_funcs = get_handler(user_input[0])(user_input)
        print(result_funcs)


COMMANDS = {
    "hello": hello_func,
    "add": add_name_and_phone_number,
    "change": change,
    "phone": phone,
    "show_all": show_all,
    "del": del_contact,
    "help": show_help,
}


if __name__ == "__main__":
    main()
