def greet(name):
    print(f"Hey {name}, welcome to Amazon.")

def add_numbers(a, b):
    return a + b

name = input("What's your name? ")
greet(name)

result = add_numbers(10, "hello")
print(f"10 + 25 = {result}")