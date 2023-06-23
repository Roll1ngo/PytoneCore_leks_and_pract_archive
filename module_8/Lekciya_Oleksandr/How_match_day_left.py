from datetime import datetime

def get_days():
    """Скрипт розрахунку кількості днів до заданної дати"""

    user_input = input("ВВедіть дату у форматі dd.mm:")
    user_date = datetime.strptime(user_input,"%d.%m")
    current_day = datetime.now()
    user_date = user_date.replace(year = current_day.year)
    delta_days = user_date - current_day
    target_day = datetime.strftime(user_date,"%d %B %Y")
    print(target_day)
    if delta_days.days>0:
        print(f"{delta_days.days} днів залишилось до{target_day}")
    else:
        user_date = user_date.replace(year = user_date.year+1)
        delta_days = user_date - current_day
        print(f"{delta_days.days} днів залишилось до{target_day}")
    


if __name__ == "__main__":
    get_days()