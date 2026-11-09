#I have used Gen AI for the purposes of creating this assesment 

# First menu

print("Welcome to Budget Tracker! Please select an option from the menu below:")
print("Please select an option from the menu below using the numbers 1 - 3") #call to action


# Navigating through the first menu option
def first_menu():

    print("1 Add Income")
    print("2 Add Expense")
    print("3 View Budget Summary")

#Functions to be called on: ----------------------------------------------------------------

def income1():
    income1 = int(input(""))
    
    if income1 == 1:
        print("You have selected Add Income.")
        income2()
    
    elif income1 == 2:
        print("You have selected Add Expense.")
    elif income1 == 3:
        print("You have selected View Budget Summary.")
    else :
        print("Invalid option selected. Please select a number between 1 - 3.")

# Adding incomes by naviating through the second income menu option ------------------------
      
def income_2():

    print("What type of income is this?")
    print("Please select an option from the menu below using the numbers 1 - 2") #call to action
    print("\n1 Salary,\n2 Other Income")


    income2 = int(input(""))
    if income2 == 1:
        salary = float(input("Please enter the amount of your salary: "))
    elif income2 == 2:
        otherincome = float(input("Please enter the amount of your other income: "))
        print("£",otherincome, "has been added to your tracker")
    else:
        print("Invalid option selected. Please select a number between 1 - 2.")


# Adding expenses by navigating through the second expense menu option ---------

def expense1():

    print("What type of expense is this?")
    print("Please select an option from the menu below using the numbers")
    print("\n1 House utilites, \n2 Personal Expenses, \n3 Leisure, \n4 Savings \n5 Other Expenses")

    expense1 = int(input(""))

    if expense1 == 1:
        print("You have selected house utilities.")
        houseutilities = float(input("Please enter the amount of your house utilities: "))
        print("£", houseutilities, "has been added to your budget tracker.")

    elif expense1 == 2:
        print("You have selected personal expenses.")
        personalexpenses = float(input("Please enter the amount of your personal expenses: "))
        print("£", personalexpenses, "has been added to your budget tracker.")

    elif expense1 == 3:
        print("You have selected leisure.")
        leisureexpenses = float(input("Please enter the amount of your leisure expenses: "))
        print("£", leisureexpenses, "has been added to your budget tracker.")

    elif expense1 == 4:
        print("You have selected savings.")
        savings = float(input("Please enter the amount of your savings: "))
        print("£", savings, "has been added to your budget tracker.")

    elif expense1 == 5:
        print("Enter any other expenses.")
        otherexpenses = float(input("Please enter the amount of your other expenses: "))
        print("£", otherexpenses, "has been added to your budget tracker.")

    else:
        print("Invalid option selected. Please select a number between 1 - 5")


#personal bill menu ----------------------------------------------------------------

def personal_bills():

    print("what type of personal bill is this?")
    print("Please select an option from the menu below using the numbers")
    print("\n1 Phone, \n2 Fuel, \n3 Subscriptions, \n4 Food \n5 Other")

    personal_bills = int(input(""))

    if personal_bills == 1:
        print("You have selected phone.")
        phone = float(input("Please enter the amount of your phone bill: "))
        print("£", phone, "has been added to your budget tracker.")
    elif personal_bills == 2:
        print("You have selected fuel.")
        fuel = float(input("Please enter the amount of your fuel expenses: "))
        print("£", fuel, "has been added to your budget tracker.")
    elif personal_bills == 3:
        print("You have selected subscriptions.")
        subscriptions = float(input("Please enter the amount of your subscriptions: "))
        print("£", subscriptions, "has been added to your budget tracker.")
    elif personal_bills == 4:
        print("You have selected food.")
        food = float(input("Please enter the amount of your food expenses: "))
        print("£", food, "has been added to your budget tracker.")
    else :
        print("Invalid option selected. Please select a number between 1 - 5")

#Leisure bill menu ----------------------------------------------------------------

def leisure_bills():

    print("what type of leisure bill is this?")
    print("Please select an option from the menu below using the numbers between 1-4")
    print("\n1 Eating/Drinking out, \n2 Clothes, \n3 Hobbies, \n4 Other")

    leisure_bills = int(input(""))

    if leisure_bills == 1:
        print("You have selected Entertaintment")
        entertaintment = float(input("Please enter the amount of your entertaintment expenses: "))
        print("£", entertaintment, "has been added to your budget tracker.")
    elif leisure_bills == 2:
        print("You have selected Clothes")
        clothes = float(input("Please enter the amount of your clothes expenses: "))
        print("£", clothes, "has been added to your budget tracker.")
    elif leisure_bills == 3:
        print("You have selected Hobbies")
        hobbies = float(input("Please enter the amount of your hobbies expenses: "))
        print("£", hobbies, "has been added to your budget tracker.")
    elif leisure_bills == 4:
        print("You have selected Other")
        other = float(input("Please enter the amount of any other expenses: "))
        print("£", other, "has been added to your budget tracker.")
    else:
        print("Invalid option selected. Please select a number between 1 - 4")


#Housing bill menu 

def housing_bills():

    print("what type of housing bill is this?")
    print("Please select an option from the menu below using the numbers between 1-6. ")
    print("\n1 Rent,\n2 Electricity,\n3 Gas, \n4 Council Tax, \n5 Water, \n6 Other ")

    housing_bills = int(input (""))

    if housing_bills == 1:
        print("You have selected Rent")
        rent = float(input("Please enter your Rent"))
        print( )















        
def savings():
    print("You have selected savings.")
    savings = float(input("Please enter the amount of your savings: "))
    savingscomment = input("Please enter a comment for your savings: ")
    print ("£" + str(savings) + "0" +" " + ": "+ savingscomment + " has been put into Savings") 

def otherexpense():
    print ("You have selected other expenses.")
    others = float(input("Please enter what other expenses you have: "))
    otherscomment = input("Please enter a comment for this expense: ")
    print ("£" + str(others) + "0" + " " + ": " + otherscomment + " has been put into Other Expenses")


while True:
    menu=

    