def calc(first, second, operation):
    if operation == '+':
        return first + second
    elif operation == '-':
        return first - second
    elif operation == '/':
        return first / second
    elif operation == '*':
        return first * second


def operation_decorator(func):
    def wrapper(first, second, operation):
        if first < 0 or second < 0:
            operation = "*"
        elif first == second:
            operation = '+'
        elif first > second:
            operation = '-'
        elif second > first:
            operation = "/"
        return func(first, second, operation)
    return wrapper


@operation_decorator
def calc_use_dec(first, second, operation):
    return calc(first, second, operation)


first = int(input('Please input the first number: '))
second = int(input('Please input the second number: '))

result = calc_use_dec(first, second, '')
print(f"Result: {result}")
