#!/usr/bin/python3
def fizzbuzz():
    for number in range(1, 101):  # Consider numbers from 1 to 100
        if number % 3 == 0 and number % 5 == 0:
            print("FizzBuzz")
        elif number % 3 == 0:
            print("Fizz")
        elif number % 5 == 0:
            print("Buzz")
        else:
            print(number)

# Call the fizzbuzz function to execute it
fizzbuzz()


