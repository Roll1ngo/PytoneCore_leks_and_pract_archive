from faker import Faker
from normalize import normalize
import json
from functools import wraps

fake = Faker("uk-UA")
Faker.seed(1)


def faker_dict() -> dict:
    contacts_dict = dict()

    for i in range(10):
        contacts_dict[normalize(fake.name().lower())] = fake.phone_number()

    return contacts_dict


def input_error(func):
    def inner_func(*args, **kwargs):
        try:
            result = func(*args, **kwargs)

            return result
        except IndexError:
            print("Input command name(nospase, example: firstname_lastname) phone")
        except TypeError:
            print("Input>>> command name(example:firstname_lastname) phone")
        except KeyError:
            print("Name not found, check spelling or use command 'show_all' ")
        except ValueError:
            print("Input>>> command name(example:firstname_lastname) phone")

    return inner_func


def hello_func(user_input: str) -> str:
    return "How can I help you"


def phone(user_input: str) -> str:
    return contacts[user_input[1]]


def show_all(user_input: str) -> dict:
    return contacts


def add_name_and_phone_number(user_input: str) -> dict:
    contacts[normalize(user_input[1])] = user_input[2]

    with open("phone_book.json", "w") as file:
        json.dump(contacts, file)

    return f"contact {user_input[1].capitalize()} which has the number {user_input[2]} add to phone book"


def change(user_input: str) -> dict:
    value = contacts.pop(user_input[1])
    contacts[normalize(user_input[1])] = user_input[2]

    with open("phone_book.json", "w") as file:
        json.dump(contacts, file)

    return (
        f"{user_input[1].capitalize()}:{value} changed phone number to {user_input[2]}"
    )


def get_handler(command: str) -> str:
    return COMMANDS[command]


@input_error
def main():
    while True:
        user_input = input(">>>").lower()
        if user_input in abort_list:
            print("Good bye! Have a nice day!")
            break
        user_input = user_input.strip().split()
        result_funcs = get_handler(user_input[0])(user_input)
        print(result_funcs)


if __name__ == "__main__":
    with open("phone_book.json", "r") as file:
        contacts = json.load(file)

    COMMANDS = {
        "hello": hello_func,
        "add": add_name_and_phone_number,
        "change": change,
        "phone": phone,
        "show_all": show_all,
    }
    abort_list = ["good bye", "close", "exit"]

    main()
