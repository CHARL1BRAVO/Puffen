# Which number do you want to check?
number = int(input())

def is_even(number):
    return number % 2 == 0

def is_odd(number):
    return number % 2 != 0

if is_even(number):
    print("This is an even number.")
else:
    print("This is an odd number.")