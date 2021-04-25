import random
import user_class
from wheezy.core.feistel import make_feistel_number
from wheezy.core.feistel import sample_f


def getUniqueNumber():

    unique = False 
    while not unique:
        num = random.randrange(1,user_class.User.maxUsers)
           
        if(user_class.User.checkId_num(num) == True):
            unique = True   
    return num



def grabDate():
    while True:
        date = input("Please enter a user's DOB: [mm/dd/yy] ")
        if( len(date) == 8 and date[2] == "/"):
            return date
        else:
            print("Incorrect date format!\nEnter date as: [mm/dd/yy] ")

        
def num_there(s):
    return any(i.isdigit() for i in s)



def loadDatabase():
 
    user_class.User.loadUsers()
    


def display_home_message():

    print("\nWelcome to User Management System")
    s = input("""Would you like to __
          1 - See Current Users
          2 - Register a User
          3 - Delete User
          4 - Show a User
          

    return s
def generate_account():
    num = random.randrange(1,user_class.User.maxUsers)
    feistel_number = make_feistel_number(sample_f + num)
    print("\n Your account number is {} ".format(feistel_number))

def option1():
    print("- How much would you like to withdraw")
    amount_withd=int(input())
    #curr_balance = amounts - amount_withd
    print("take your cash")

def option2():
    print("- How much would you like to deposit? ")
    amount_depos=int(input())
    amounts.append(amount_depos)
    curr_balance = int((amounts[0] +  amount_depos))
    print("Your current balance is:", curr_balance)

def complaint():
     print("-What issue will you like to report? ")
     issue =input()
     print("Thank you for contacting us")
    

OptionSelect = {

    1:option1,
    2:option2,
    3:complaint

}
