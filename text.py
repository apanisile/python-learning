#This python material is the learning process

#course = 'Python for Beginners'
#print the length of the string
#print(len(course))

#----------------------------------------------------------------------------------------------

#methods thst can beused for strings
##course.upper() cpnverts to upper
##course.lower() converts to lower
#course.title()
#course.find()
#course.replace(x, y)
#'...' in course

#----------------------------------------------------------------------------------------------

#print(course.replace('Beginners', 'Absolute Beginners'))
#print('python' in course)

#----------------------------------------------------------------------------------------------

#Arithmatic Operators
#Divide
#print(10/3)

#Modulus
#print(10%3)

#Exponential
#print(10 ** 3)


#----------------------------------------------------------------------------------------------


#Augumented assignment operator
#Addition
#x = 10
#x = x + 3
#x += 3
#print(x)

#Subraction
#x = 10
#x -= 3
#print(x)


#Operator Precedence (order of operations (BODMAS))
#Parenthesis
#Exponentiation 2 ** 3
#multipliction or division
#addition or subtraction

#x = 10 + 3 * 2 ** 2
#print(x)

#----------------------------------------------------------------------------------------------

#Math Functions
#x= 2.9
#print(round(x))

#absolute always returns a positive function
#x = -2.9
#print(abs(x))

#modules are seperate files with re-useable code
#import math
#print(math.floor(2.9))

#----------------------------------------------------------------------------------------------

#If statements
#is_hot = False
#is_cold = False

#if is_hot:
 #   print("It's a hot day")
  #  print("Drink plenty of water")
#elif is_cold:
#    print("It's a cold day")
#    print("Wear warm clothes")
#else:
#    print("Its a lovely day")
#
#print("Enjoy your day")


#price = 1000000
#has_good_credit = input("Do you have good credit?")
#has_good_credit = False

#if has_good_credit:
#    down_payment = 0.1 * price
#else:
#    down_payment = 0.2 * price
#print(f"The down payment for the house you need to pay is ${down_payment}")


##Logical Operators
#has_high_income = False
#has_good_credit = True

#AND: both
#OR: at least ine
#NOT

#if has_high_income and has_good_credit:
#    print("Eligible for loan")
#if has_high_income or has_good_credit:
#    print("Eligible for loan")

#has_criminal_record = False
#has_good_credit = True

#if has_good_credit and not has_criminal_record:
#    print("Eligible for loan")

#----------------------------------------------------------------------------------------------
#Comparison Operators
#> #< #>= #== #!=
#temperature = 35

#if temperature > 30:
#    print("It's a hot day")
#else:
#    print("It's not a hot day")

#----------------------------------------------------------------------------------------------
###CLASSWORK
#name = input("DO enter your name: ")
#if len(name) < 3:
#    print("Name must be at least 3 characters long")
#elif len(name) >= 50:
#    print("Name can be maximum of 50 characters")
#else:
#    print("Name looks good!")

#----------------------------------------------------------------------------------------------

#######Project: Weight Converter
#weight = int(input("Input your weight: "))
#unit = input("(L)bs or (K)g: ")
#if unit.upper() == "L":
#    converted = weight * 0.45
#    print(f"You are {converted} kilos")
#else:
#    converted = weight / 0.45
#    print(f"You are {converted} pounds")


#----------------------------------------------------------------------------------------------
#While loops
#i = 1
#while i<=5:
#    print("*" * i)
#    i = i + 1
#print("Done")
#----------------------------------------------------------------------------------------------

###Guessing game
#secret_number = 9
#guess_count = 0
#guess_limit = 3
##while guess_count < guess_limit:
 #   guess =  int(input("Guess: "))
 #   guess_count += 1
 #   if guess == secret_number:
 #       print("You won!")
 ##       break
  #  else:
  #      print("Try again!")
#else:
#    print("Sorry you failed!")
#-----------------------------------------------------------------------------------------------

##Car Game
#help
#start- to start the car
#stop - to stop the car
#quit - to exit

#any other thing
#I don't understand that...
#start
#Car started...Ready to go!
#stop
#Car stopped.
#quit
#exit


#keyword = input("Type help to access car commands: ")
#if keyword.upper() == "HELP":
#    print("start- to start the car")
#    print("stop - to stop the car")
#    print("quit - to exit")
#elif keyword == "start" or "START":
#    print("Car started...Ready to go!")
#else:
#    print("I don't understand!")


#command = ""
#started = False
#while True:
#    command = input("> ").upper()
#    if command == "START":
#        if started:
#           print("Car is already started!")
#        else:
#            started = True
#            print("Car started...Ready to go!")
#    elif command == "STOP":
#        if not started:
#            print("Car is already stopped!")
#        else:
#            started = False
#            print("Car stopped!")
#    elif command == "HELP":
#        print("""
#start- to start the car
#stop - to stop the car
#quit - to exit
#            """)
#    elif command == "QUIT":
#        break
#    else:
#        print("Sorry! I don't understand...")

#-----------------------------------------------------------------------------------------------
#For loops
#for item in range(500, 1000, 3):
    #this produces nummbers from 500 - 999 while skipping 3's
#    print(item)

#Exercise
#prices = [10,20,30]
#total = 0
#for price in prices:
#    total += price
#print(f"Total: {total}")
#-----------------------------------------------------------------------------------------------

##Nested Loops
#The values in "y" would keep running for every instance of "x"
#for x in range(4):
##    for y in range(3):
##        print(f'({x}, {y})')

#-----------------------------------------------------------------------------------------------
#numbers = [5,2,5,2,2]
#value = input("Value")
#for item in numbers:
   #print("x" * item)
#    output = " "
#    for count in range(item):
#        output += 'x'
##    print(output)
#2D lista
#-----------------------------------------------------------------------------------------------
#nested for loops to print out "L"
#numbers = [1,1,1,1,5]
#for x_count in numbers:
#    output = ""
#    for count in range(x_count):
#        output += 'x'
#    print(output)
#-----------------------------------------------------------------------------------------------
#Lists
#room = ['Ife', 'Messi', 'Labile', 'Sawyerr', 'Draggs', 'Biola']
#room[0] = 'Oluchi'
#print(room)
#-----------------------------------------------------------------------------------------------
#Write a program to find the largest number in a list
#numbers = [0,7,8,11,9,3,56,88,100]
#max = numbers[0]
#for number in numbers:
 #   if number > max:
 #       max = number
#print(max)
#-----------------------------------------------------------------------------------------------
#2D Lists
#[
#    1 2 3
#    4 5 6
#    7 8 9
#]
#matrix = [
#            [1,2,3],
#            [4,5,6],
#            [7,8,9]
#]
#matrix[0][1]  = 20
#print(matrix[0][1])

#for row in matrix:
#    for item in row:
#        print(item)

#numbers = [5,2,1,7,4,5,6]
#numbers.append(20)
#numbers.insert(2, 10)
#numbers.remove(4)
#numbers.clear()
#numbers.pop()
#print(numbers.index(5))
#print(numbers)
#print(7 in numbers)
#print(numbers.count(5))
#numbers.sort()
#numbers.reverse()
#numbers2 = numbers.copy()
#numbers.append(10)
#print(numbers)
#print(numbers2)


##Execrise
#print("Write a program to remove the duplicates in a list:")
#numbers= [2,2,5,6,3,4,2,6]
#no_dups = []
#for number in numbers:
#    if number not in no_dups:
#        no_dups.append(number)
#print(no_dups)
#-----------------------------------------------------------------------------------------------
#Tuples
#Tuples cannot be changed
#numbers = (1, 2, 3)
#print(numbers[0])
#-----------------------------------------------------------------------------------------------
#Unpacking
#coordinates = (1, 2, 3)
#x = coordinates[0]
#y = coordinates[1]
#z = coordinates[2]

#x,y,z = coordinates
#print(z)
#-----------------------------------------------------------------------------------------------
#Dictionaries
