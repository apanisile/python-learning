#Python program to calculate loan
import user_details
from user_details import *
        
user = loan_function()
user.name()
user.email()

bank_credit = int(input("Please what is your bank credit score? "))

bench_mark = 10000

if bank_credit >= bench_mark :
    user.payment()
else:
    print(f"Sorry! You do not qualify for our bank loan")
    