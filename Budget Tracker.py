# First menu

print("Welcome to Budget Tracker! Please select an option from the menu below using the numbers 1 - 3:")

print("1 Add Income")
print("2 Add Expense")
print("3 View Budget Summary")

#navigatin through the first menu option

a = int(input(""))

if a == 1:
    print("You have selected Add Income.")
elif a == 2:
    print("You have selected Add Expense.")
elif a == 3:
    print("You have selected View Budget Summary.")

 
print("What type of income is this?")
print("\n1 Salary,\n2 Other Income")

#adding incomes by naviating through the second menu option
      
b = int(input(""))

if b ==1:
    print(input("Please enter the amount of your salary: "))
if b == 2:
    print(input("Please enter the amount of your other income: "))

