#Python program to calculate loan
def greet(fname, lname, msg="Good morning!"):
    """
    This function greets to
    the person with the
    provided message.

    If the message is not provided,
    it defaults to "Good
    morning!"
    """
    print("Hello", fname + ' '+ lname + ', ' + msg)
    
def valid(x, y):
    
    if x != y:
        print("the numbers are not the same")
        exit(1)
    else: 
        print("Accepted")
        
        
fname = input("Hi there! Please enter your first name: ")
lname = input("Please enter your last name: ")

greet (lname, fname)

email = input("Enter your e-mail address: ")
email2 = input("Enter your e-mail address again: ")

if email != email2:
    print("The email's dont match")
    exit(1)

bank_credit = int(input("Please what is your bank credit score? "))

bench_mark = 10000

if bank_credit >= bench_mark :
    print("Great! you qualify for a loan! ")
    print("What payment method would you prefer: ")
    payment_method= int(input("""
    1. Direct Deposit
    2. Wire Check
    3. Transfer """))
    
    if payment_method == 1:
        
        bank_name = input("Enter bank name: ")

        routing_no = input("Enter your routing number: ")
        routing_no1 = input("Enter your routing number again: ")
        valid(routing_no, routing_no1)
        
        acct_no = input("Enter your account number: ")
        acct_no1 = input("Enter your account number again: ")
        valid(acct_no, acct_no1)
        
    elif payment_method == 2:
        print("You hae chosen the Wire Check option")
        account_name = input("What name shoudl be written on the check?: ")
        
    elif payment_method == 3:
        print("You have chosen the transfer option!")
    else:
        print("There is no option like that")
        exit(1)
        
else:
    print(f"Sorry {lname} {fname}! You do not qualify for our bank loan")
    