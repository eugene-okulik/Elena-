x = 65
while True:
    user_input = int(input('Guess the number, please: '))
    if user_input == 'Exit' or user_input == 'exit':
        break
    elif user_input == x:
        print('Congrats! You got it')
        break
    else:
        print('Nope.Try again, please')
