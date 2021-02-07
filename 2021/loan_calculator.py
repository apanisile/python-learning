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
    
def routing(x, y):
    
    if x != y:
        print("the routing numbers are not the same")
        exit(1)
    else: 
        print("Welcome")
        
        
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
    payment_method= input("""
    1. Direct Deposit
    2. Wire Check
    3. Transfer""")
    
    if payment_method == 1:

        routing_no = input("Enter your routing number: ")
        routing_no1 = input("Enter your routing number again: ")
        routing(routing_no, routing_no1)
        
else:
    print(f"Sorry {lname} {fname}! You do not qualify for our bank loan")
    