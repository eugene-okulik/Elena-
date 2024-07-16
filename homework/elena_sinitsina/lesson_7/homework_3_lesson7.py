
def print_new_numbers(numbers):
    for number in numbers:
        x = int(number.split(': ')[1])
        x += 10
        print(x)


numbers = ['результат операции: 42', 'результат операции: 54', 'результат работы программы: 209', 'результат: 2']
print_new_numbers(numbers)
