def fibonacci_generator():
    fib_list = [0, 1]
    while True:
        next_value = fib_list[-1] + fib_list[-2]
        fib_list.append(next_value)
        yield next_value


fib_gen = fibonacci_generator()


def fibonacci_number(n):
    fib_list = [0, 1]
    while len(fib_list) < n:
        fib_list.append(fib_list[-1] + fib_list[-2])
    return fib_list[n - 1]


print("5th Fibonacci number:", fibonacci_number(5))
print("200th Fibonacci number:", fibonacci_number(200))
print("1000th Fibonacci number:", fibonacci_number(1000))
print("10000th Fibonacci number:", fibonacci_number(10000))
