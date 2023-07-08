from faker import Faker

fake = Faker("uk-UA")
Faker.seed(1)


def faker_dict() -> list:
    contacts_dict = dict()

    for i in range(3):
        contacts_dict[fake.name()] = fake.phone_number()

    return contacts_dict


def hello_func(user_input):
    print("How can I help you")


def add_name_and_phone_number(user_input: str) -> dict:
    users[user_input[1].capitalize()] = user_input[2]


def get_handler(command: str) -> None:
    return COMMANDS[command]


def main():
    while True:
        user_input = input(">>>").lower()
        if user_input in abort_list:
            print("Have a nice day")
            break
        user_input = user_input.strip().split()
        result_func = get_handler(user_input[0])(user_input)


if __name__ == "__main__":
    users = faker_dict()

    COMMANDS = {"hello": hello_func, "add": add_name_and_phone_number}
    abort_list = ["good bye", "close", "exit"]
    main()
