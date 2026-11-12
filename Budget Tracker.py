#I have used Gen AI for the purposes of checking and my reviewing my work in this assessment.

#importing CSV 
import csv
from pathlib import Path
from datetime import date

BASE_DIR = Path(__file__).resolve().parent
CSV_FILE = BASE_DIR / "budgettracker.csv"


#Saving data to CSV 

def savedata(amount, transaction_type ,category):
    transaction_date = date.today().strftime("%m/%Y")
    with open(CSV_FILE, "a", newline="") as f:   
        writer = csv.writer(f)
        writer.writerow([amount, transaction_type, category, transaction_date])  # list created with the amount of money inputted, type is sub category, category is type of income/expense  and date 





# Introduction


    # Navigating through the first menu option
def first_menu():

        print("1 Add Income")
        print("2 Add Expense")
        print("3 View Budget Summary")
        print("4 Exit")

    #Functions to be called on: 

    # Adding incomes by naviating through the second income menu option 
def income_1():
        print("Please first enter your income.")
        print("What type of income is this?")
        print("Please select an option from the menu below using the numbers 1 - 2. Press any other chracter to go back to the main menu")
        print("\n1 Income, \n2 Other")
       


        incomechoice = int(input(""))
        if incomechoice == 1:
            salary = float(input("Please enter the amount of your salary: "))
            print("£",salary, "has been added to your tracker. Please press a button to continue" )
            
        elif incomechoice == 2:
            otherincome = float(input("Please enter the amount of your other income: "))
            print("£",otherincome, "has been added to your tracker. Please press a button to continue")
            
        else:
            first_menu()

def income_2():
        income_2 = int(input(""))
        
        if income_2 == 1:
            print("You have selected Add Income.")
            income_1()
        elif income_2 == 2:
            print("You have selected Add Expense.")
        elif income_2 == 3:
            print("You have selected View Budget Summary.")
        else:
            print("Invalid option selected. Please select a number between 1 - 3.")

# Introduction

def intro():

    print("Welcome to Budget Tracker!")
    income_1()

    # Adding expenses by navigating through the second expense menu option

def expense1():

    print("1 House Utilities")
    print("2 Personal Expenses")
    print("3 Leisure")
    print("4 Savings")
    print("5 Other Expenses")

    expense_choice = input("")
    return expense_choice        


#Housing bill menu 

def housing_bills():

        print("what type of housing bill is this?")
        print("Please select an option from the menu below using the numbers between 1-6. ")
        print("\n1 Rent,\n2 Electricity,\n3 Gas, \n4 Council Tax, \n5 Water, \n6 Other ")

        housing_bills = int(input (""))

        if housing_bills == 1:
            print("You have selected Rent")
            rent = float(input("Please enter your Rent:"))
            savedata(rent, "Expense", "Rent")
            print("£", rent, "has been added to your budget tracker." )
        elif housing_bills == 2:
            print ("You have selected Electricity.")
            electricity = float(input("Please enter the amount for your Electricity:"))
            print("£", electricity, "has been added to your budget tracker.")
        elif housing_bills == 3:
            print ("You have selected Gas.")
            gas = float(input("Please enter the amount for your Gas:"))
            print("£", gas, "has been added to your budget tracker.")
        elif housing_bills == 4:
            print ("You have selected Council Tax.")
            electricity = float(input("Please enter the amount for your Council Tax:"))
            print("£", electricity, "has been added to your budget tracker.")
        elif housing_bills == 5:
            print ("You have selected Council Water.")
            water = float(input("Please enter the amount for your Water:"))
            print("£", water, "has been added to your budget tracker.")
        elif housing_bills == 6:
            print ("You have selected Other.")
            otherh = float(input("Please enter the amount for your Council Tax:"))
            print("£", otherh, "has been added to your budget tracker.")
        else:
            print("Invalid option selected. Please select a number between 1 - 6")


    #Personal bill menu 

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
        elif personal_bills == 5:
                print ("You have selected other.")
                otherp = float(input("Please enter the amount for your Council Tax."))
                print("£", otherp, "has been added to your budget tracker.")
                
        else :
            print("Invalid option selected. Please select a number between 1 - 5")

    #Leisure bill menu 

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
            otherl = float(input("Please enter the amount of any other expenses: "))
            print("£", otherl, "has been added to your budget tracker.")
        else:
            print("Invalid option selected. Please select a number between 1 - 4")

#savingsmenu
          
def savings():
        print("You have selected savings.")
        savings = float(input("Please enter the amount of your savings: "))
        savingscomment = input("Please enter a comment for your savings: ")
        print ("£" + str(savings) + "0" +" " + ": "+ savingscomment + " has been put into Savings") 

#other expense menu

def otherexpense():
        print ("You have selected other expenses.")
        others = float(input("Please enter what other expenses you have: "))
        otherscomment = input("Please enter a comment for this expense: ")
        print ("£" + str(others) + "0" + " " + ": " + otherscomment + " has been put into Other Expenses")

#Navigation menu
intro()

while True:
    first_menu()

    menu = input("")

    if menu == "1":
            income_1()
    elif menu == "2":
            expense_choice = expense1()
            
            if expense_choice == "1":
                housing_bills()
            elif expense_choice == "2":
                personal_bills() 
            elif expense_choice == "3":
                leisure_bills()  
            elif expense_choice == "4":
                savings()
            else:
                print("Returning to main menu")
                continue

    elif menu == "3":
        print("You have selected View Budget Summary")
    elif menu == "4":
         print("You have exited Budget Tracker!")
         break
    else:
        print("Invalid valid option. Returning to main menu.")
        continue