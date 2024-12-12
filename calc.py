
menu = {"add": 1,
        "subtract": 2,
        "multiply": 3,
        "divide": 4
        }
def display_menu():
    for key, value in menu.items():
        print(f"{value}: {key}")

display_menu()

option = input("Select the option: ")

num1 = float(input("Please enter your first number: "))
num2 = float(input("Please enter your second number: "))


if option == "1":
    total = num1 + num2
    print(f"{num1} + {num2} = {total}")
elif option == "2":
    total = num1 - num2
    print(f"{num1} - {num2} = {total}")
elif option == "3":
    total = num1 * num2
    print(f"{num1} * {num2} = {total}")
elif option == "4":
    if num2 != 0:
        total = num1 / num2
        print(f"{num1} / {num2} = {total}")
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Invalid option selected.")