#Python program to calculate laon eligibility

fname = input("Hi there! Please enter your first name: ")
lname = input("Please enter your last name: ")

bank_credit = int(input("Please what is your bank credit score? "))

bench_mark = 10000

if bank_credit >= bench_mark :
    print("""Great! you qualify for a $5000 loan! How would you want to collect your loan?""")
    loan = input("Great! How much would you like to loan?: ")
    
else:
    print(f"Sorry {lname} {fname}! You do not qualify for our bank loan")
    