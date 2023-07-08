from datetime import datetime, timedelta
from faker import Faker
from faker.providers import person
from rich import print


fake = Faker("uk-UA")
fake.add_provider(person)


def faker_dict() -> list:
    users = list()

    for i in range(50):
        fake_persons = dict()
        fake_persons["name"] = fake.name()
        fake_persons["birthdate"] = fake.profile()["birthdate"]
        users.append(fake_persons)

    return users


def get_correct_week_day(bd: datetime) -> str:
    if bd.weekday() >= 5:
        day = bd.replace(day=bd.day + (7 - bd.weekday()))
        day_of_week = day.strftime("%A")

    else:
        day_of_week = bd.strftime("%A")

    return day_of_week


def get_period() -> tuple[datetime.date, datetime.date]:
    current_date = datetime.now()
    start_period = current_date + timedelta(days=5 - current_date.weekday())
    return start_period.date(), start_period.date() + timedelta(days=6)


def get_birthdate_per_week() -> list:
    user_list = faker_dict()
    current_year = datetime.now().year
    birthdate_list = []

    for user in user_list:
        bd_dict = dict()
        bd = user["birthdate"]
        bd = bd.replace(year=current_year)
        start, end = get_period()

        if start <= bd <= end:
            day_for_congratulations = get_correct_week_day(bd)
            bd_dict[day_for_congratulations] = user["name"]
            birthdate_list.append(bd_dict)

    return birthdate_list


if __name__ == "__main__":
    print(get_birthdate_per_week())
