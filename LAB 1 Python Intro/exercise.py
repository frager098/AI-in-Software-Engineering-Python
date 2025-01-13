# Exercise
# Create a Python Program that perform following tasks for any problem of your choice:
# Task 1: Introduction
# Task 2: Terminal
# Task 3: Python Interpreter
# Task 4: Variables
# Task 5: Text Editor
# Task 6: Functions
# Task 7: Lists and Tuples
# Task 8: Conditional Statements
# Task 9: The For Loop
# Task 10: User Input and the While Loop


# Task 1: Introduction
print("Welcome to the Python Fundamentals Demo Program!")
print("This program demonstrates various Python concepts using a simple problem.")

# Task 2: Terminal
name = input("Enter your name: ")
print(f"Hello, {name}! Let's start exploring Python.")

# Task 3: Python Interpreter (implied by running this script)

# Task 4: Variables
age = int(input("Enter your age: "))
next_year_age = age + 1
print(f"Next year, you will be {next_year_age} years old.")

# Task 5: Text Editor (implied by saving and running this script)

# Task 6: Functions
def greet_user(name):
    print(f"Hello, {name}! Welcome to the program.")
greet_user(name)

# Task 7: Lists and Tuples
fruits = ["apple", "banana", "cherry"]
print("Available fruits:", fruits)
numbers = (1, 2, 3)
print("Tuple of numbers:", numbers)

# Task 8: Conditional Statements
if age < 18:
    print("You are a minor.")
elif age == 18:
    print("You just turned an adult!")
else:
    print("You are an adult.")

# Task 9: The For Loop
print("Counting from 1 to 5:")
for i in range(1, 6):
    print(i)

# Task 10: User Input and the While Loop
while True:
    choice = input("Enter 'exit' to quit or anything else to continue: ")
    if choice.lower() == 'exit':
        print("Goodbye!")
        break
    else:
        print("You entered:", choice)
