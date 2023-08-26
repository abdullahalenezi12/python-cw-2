my_name = input('Whats your name? ')
my_age = input('How old are you? ')
print(f'My name is {my_name}, and i am {my_age} years old')

stateofwhile = 1

while stateofwhile:
    num1 = int(input('What is the first number? '))
    num2 = int(input('What is the second number? '))
    operation = input('What is the operation ')
    if '+' in operation:
        answer = num1 + num2
    elif '-' in operation:
        answer = num1 - num2
    elif 'x' in operation:
        answer = num1 * num2
    elif '/' in operation:
        answer = num1 / num2
    print(f'{num1} {operation} {num2} = {answer}')
    keepgoing = input('Would you like to keep going? ')
    if keepgoing == 'yes':
        stateofwhile = 1
    else:
        print('Thank you for using my calclulator!')
        break   


bus_capacity = 30
people_inbus = int(input('How many people are on the bus? '))
people_who_want_to_getonbus = int(input('How many people want to get on the bus? '))
empty_seats = bus_capacity - people_inbus
if empty_seats >= people_who_want_to_getonbus:
    print("There are enough seats!")
else:
    print('There arent enough seats.')