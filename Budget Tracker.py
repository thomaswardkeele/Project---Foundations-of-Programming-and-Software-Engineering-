#I have used Gen AI for the purposes of creating this assesment 

# First menu

print("Welcome to Budget Tracker! Please select an option from the menu below:")
print("Please select an option from the menu below using the numbers 1 - 3") #call to action


# Navigating through the first menu option
print("1 Add Income")
print("2 Add Expense")
print("3 View Budget Summary")

#Functions to be called on: ------------------------------------------------------------------------------------------------- 

def income1():
    a = int(input(""))
    
    if a == 1:
        print("You have selected Add Income.")
    elif a == 2:
        print("You have selected Add Expense.")
    elif a == 3:
        print("You have selected View Budget Summary.")
    else :
        print("Invalid option selected. Please try again.")

# Adding incomes by naviating through the second income menu option ------------------------------------------------------------
      



def income2():

print("What type of income is this?")
print("Please select an option from the menu below using the numbers 1 - 2") #call to action
print("\n1 Salary,\n2 Other Income")


    b = int(input(""))
    if b == 1:
        print(input("Please enter the amount of your salary: "))
    elif b == 2:
            print(input("Please enter the amount of your other income: "))
    else :
        print("Invalid option selected. Please try again.")


# Adding expenses by navigating through the second expense menu option ------------------------------------------------------------

print("What type of expense is this?")
print("Please select an option from the menu below using the numbers")
print("\n1 House utilites, \n2 Personal Expenses, \n3 Leisure, \n4 Savings \n5 Other Expenses")

def expense1():

print("What type of expense is this?")
print("Please select an option from the menu below using the numbers")
print("\n1 House utilites, \n2 Personal Expenses, \n3 Leisure, \n4 Savings \n5 Other Expenses")


    c = int(input(""))

    if c == 1:
        print(input("You have selected house utilities."))
    elif c== 2:
        print(input("You have selected personal expenses."))
    elif c == 3:
        print(input("You have selected leisure."))
    elif c == 4:      
        print(input("You have selected savings."))
    elif c == 5:
        print(input("Enter any other expenses."))
    else :
        print("Invalid option selected. Please try again.")

#personal bill menu ---------------------------------------------------------------------------------------------------------------

def personalbills():

    print("what type of personal bill is this?")
    print("Please select an option from the menu below using the numbers")
    print("\n1 Phone, \n2 Fuel, \n3 Subscriptions, \n4 Food \n5 Other")

    d = int(input(""))

    if d == 1:
        print(input("You have selected phone."))
    elif d == 2:
        print(input("You have selected fuel."))
    elif d == 3:
        print(input("You have selected subscriptions."))
    elif d == 4:
        print(input("You have selected food."))
    else :
        print("Invalid option selected. Please try again.")
