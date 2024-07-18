import random


def calculate_bonus():
    salary = int(input('Please input your salary: '))
    bonus = random.choice([True, False])
    if bonus:
        random_bonus = random.randint(1, 20000)
        print(f'{salary}, True -${random_bonus}')
    else:
        print(f'{salary}, False -${salary}')


calculate_bonus()
