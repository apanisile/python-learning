import test2
from test2 import *

#the name part
mk = personnel()
#tim = mk.name()

#the email
mk = personnel()
#tim = mk.email()

bank_credit = int(input("Please what is your bank credit score? "))

bench_mark = 10000

if bank_credit >= bench_mark :
    mk.payment()
else:
    print(f"Sorry! You do not qualify for our bank loan")
    