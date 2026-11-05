#I have used Gen AI for the purposes of creating this assesment 

# First menu

print("Welcome to Budget Tracker! Please select an option from the menu below:")
print("Please select an option from the menu below using the numbers 1 - 3") #call to action


# Navigating through the first menu option
print("1 Add Income")
print("2 Add Expense")
print("3 View Budget Summary")

#Functions to be called on: --------------------

def income1():
    a = int(input(""))
    
    if a == 1:
        print("You have selected Add Income.")
    elif a == 2:
        print("You have selected Add Expense.")
    elif a == 3:
        print("You have selected View Budget Summary.")
    else :
        print("Invalid option selected. Please select a number between 1 - 3.")

# Adding incomes by naviating through the second income menu option ------------------------
      
def income2():

    print("What type of income is this?")
    print("Please select an option from the menu below using the numbers 1 - 2") #call to action
    print("\n1 Salary,\n2 Other Income")


    b = int(input(""))
    if b == 1:
        salary = float(input("Please enter the amount of your salary: "))
    elif b == 2:
        otherincome = float(input("Please enter the amount of your other income: "))
        print("£",otherincome, "has been added to your tracker")
    else:
        print("Invalid option selected. Please select a number between 1 - 2.")


# Adding expenses by navigating through the second expense menu option ---------


def expense1():

    print("What type of expense is this?")
    print("Please select an option from the menu below using the numbers")
    print("\n1 House utilites, \n2 Personal Expenses, \n3 Leisure, \n4 Savings \n5 Other Expenses")

    c = int(input(""))

    if c == 1:
        print("You have selected house utilities.")
        houseutilities = float(input("Please enter the amount of your house utilities: "))
        print("£", houseutilities, "has been added to your budget tracker.")

    elif c == 2:
        print("You have selected personal expenses.")
        personalexpenses = float(input("Please enter the amount of your personal expenses: "))
        print("£", personalexpenses, "has been added to your budget tracker.")

    elif c == 3:
        print("You have selected leisure.")
        leisureexpenses = float(input("Please enter the amount of your leisure expenses: "))
        print("£", leisureexpenses, "has been added to your budget tracker.")

    elif c == 4:
        print("You have selected savings.")
        savings = float(input("Please enter the amount of your savings: "))
        print("£", savings, "has been added to your budget tracker.")

    elif c == 5:
        print("Enter any other expenses.")
        otherexpenses = float(input("Please enter the amount of your other expenses: "))
        print("£", otherexpenses, "has been added to your budget tracker.")

    else:
        print("Invalid option selected. Please select a number between 1 - 5")


#personal bill menu ----------------------------------------------------------------
def personalbills():

    print("what type of personal bill is this?")
    print("Please select an option from the menu below using the numbers")
    print("\n1 Phone, \n2 Fuel, \n3 Subscriptions, \n4 Food \n5 Other")

    d = int(input(""))

    if d == 1:
        print("You have selected phone.")
        phone = float(input("Please enter the amount of your phone bill: "))
        print("£", phone, "has been added to your budget tracker.")
    elif d == 2:
        print("You have selected fuel.")
        fuel = float(input("Please enter the amount of your fuel expenses: "))
        print("£", fuel, "has been added to your budget tracker.")
    elif d == 3:
        print("You have selected subscriptions.")
        subscriptions = float(input("Please enter the amount of your subscriptions: "))
        print("£", subscriptions, "has been added to your budget tracker.")
    elif d == 4:
        print("You have selected food.")
        food = float(input("Please enter the amount of your food expenses: "))
        print("£", food, "has been added to your budget tracker.")
    else :
        print("Invalid option selected. Please select a number between 1 - 5")

#Leisure bill menu ----------------------------------------------------------------
def leisurebills():

    print("what type of leisure bill is this?")
    print("Please select an option from the menu below using the numbers")
    print("n1 Eating/Drinking out, \n2 Clothes, \n3 Hobbies, \n4 Other")

    e = int(input(""))

    if e == 1:
        print("You have selected Entertaintment")
        entertaintment = float(input("Please enter the amount of your entertaintment expenses: "))
        print("£", entertaintment, "has been added to your budget tracker.")
    elif e == 2:
        print("You have selected Clothes")
        clothes = float(input("Please enter the amount of your clothes expenses: "))
        print("£", clothes, "has been added to your budget tracker.")
    elif e== 3:
        print("You have selected Hobbies")
        hobbies = float(input("Please enter the amount of your hobbies expenses: "))
        print("£", hobbies, "has been added to your budget tracker.")
    elif e == 4:
        print("You have selected Other")
        other = float(input("Please enter the amount of any other expenses: "))
        print("£", other, "has been added to your budget tracker.")
    else:
        print("Invalid option selected. Please select a number between 1 - 4")
        
