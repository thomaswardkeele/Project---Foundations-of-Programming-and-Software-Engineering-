# First menu

print("Welcome to Budget Tracker! Please select an option from the menu below using the numbers 1 - 3:")

print("1 Add Income")
print("2 Add Expense")
print("3 View Budget Summary")

a = int(input(""))

if a == 1:
    print("You have selected Add Income.")
elif a == 2:
    print("You have selected Add Expense.")
elif a == 3:
    print("You have selected View Budget Summary.")

