import datetime
import os

file_path = 'C:/Users/Windows11/Elena-/homework/eugene_okulik/hw_13/data.txt'


def process_action(date_str, action):
    date = datetime.datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S.%f")

    if action == "распечатать эту дату, но на неделю позже. Должно получиться 2023-12-04 20:34:13.212967":
        new_date = date + datetime.timedelta(weeks=1)
        print(f"Date one week later: {new_date}")
    elif action == "распечатать какой это будет день недели":
        day_week = date.strftime("%A")
        print(f"Day of the week: {day_week}")
    elif action == "распечатать сколько дней назад была эта дата":
        current_date = datetime.datetime.now()
        delta = current_date - date
        print(f'Delta is: {delta.days}')
    else:
        print(f"Unknown action: {action}")


with open(file_path, 'r', encoding='utf-8') as file:
    lines = file.readlines()

    for line in lines:
        parts = line.split(' - ')
        if len(parts) == 2:
            left_part = parts[0].strip()
            action = parts[1].strip()
            left_parts = left_part.split(maxsplit=1)
            if len(left_parts) == 2:
                number = left_parts[0]
                date_str = left_parts[1]
                process_action(date_str, action)
