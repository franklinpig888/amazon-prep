def greet(name):
    print(f"Hey {name}, welcome to Amazon.")

def add_numbers(a, b):
    return a + b

name = input("What's your name? ")
greet(name)

result = add_numbers(10, 25)
print(f"10 + 25 = {result}")

def multiply(a, b):
    return a * b
print(multiply(4, 5))

def greet_with_time(name, time_of_day):
    print(f"Good {time_of_day}, {name}! Ready to write some code?")

greet_with_time("Frank", "morning")

