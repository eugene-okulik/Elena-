import sys
sys.set_int_max_str_digits(100000)


def progression(limit=100000):
    x = 0
    y = 1
    count = 1

    while count <= limit:
        yield x
        x, y = y, x + y
        count += 1


new_count = 1
for number in progression(100000):
    if new_count == 5:
        print(number)
    elif new_count == 200:
        print(number)
    elif new_count == 1000:
        print(number)
    elif new_count == 100000:
        print(number)
        break
    new_count += 1
