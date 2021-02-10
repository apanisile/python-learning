#Python program to calculate loan

from user_details import *

prompt_user = input("""Do you want to sign in? (Y)es or (N)o 
    > """)

if (prompt_user == "Y") | (prompt_user == "y") | (prompt_user == "yes") | (prompt_user == "Yes"):

    user = loan_function()
    user.name()
    user.email()

    bank_credit = int(input("Please what is your bank credit score? "))

    bench_mark = 10000

    while bench_mark > 0:
        if bank_credit >= bench_mark:
            user.payment()
            print("Your account would be credited in the next 2-5 working days")
        else:
            print(f"Sorry! You do not qualify for our bank loan")

else:
    print("Bye!")
    exit(0)
