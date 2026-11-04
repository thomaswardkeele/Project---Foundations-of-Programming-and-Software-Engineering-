#I have used Gen AI for the purposes of creating this assesment 

# First menu

print("Welcome to Budget Tracker! Please select an option from the menu below:")
print("Please select an option from the menu below using the numbers 1 - 3") #call to action


# Navigating through the first menu option
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

# Adding incomes by naviating through the second income menu option
      
print("What type of income is this?")
print("Please select an option from the menu below using the numbers 1 - 2") #call to action
print("\n1 Salary,\n2 Other Income")

b = int(input(""))

if b ==1:
    print(input("Please enter the amount of your salary: "))
if b == 2:
    print(input("Please enter the amount of your other income: "))

# Adding expenses by navigating through the second expense menu option

print("What type of expense is this?")
print("Please select an option from the menu below using the numbers")
print("\n1 House utilites, \n2 Personal Expenses, \n3 Leisure, \n4 Savings \n5 Other Expenses")



