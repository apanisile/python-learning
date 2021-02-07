#Python program to calculate loan
import user_details
        
user_details.name()
user_details.email()

bank_credit = int(input("Please what is your bank credit score? "))

bench_mark = 10000

if bank_credit >= bench_mark :
    user_details.payment()
else:
    print(f"Sorry! You do not qualify for our bank loan")
    