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
    
    
fname = input("Hi there! Please enter your first name: ")

lname = input("Please enter your name: ")
greet(lname, fname)

