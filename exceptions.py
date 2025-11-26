usernames = ['Cheetara', 'Lion-O', 'Snarf', 'Tygra', 'Panthro', 'Mumm-Ra']


def login_unhandled(usernumber):
    print("\n -- The Basic Version --\n")
    number = int(usernumber)
    print("Welcome", usernames[number], "user number", number,".")
    try: 
        division = 301 / number
        print(f"301 divided by {number} = {division}")
    except ZeroDivisionError:
        print("you have tried to divide a number by zero. Please restart the program")
    except OverflowError:
        print("Your number has made it so the operation has caused the resultant number to take up more space than available in memory. Please restart the program")
    print(f"301 divided by {number} = {division}")  

while True:
    inp = input("\nType in a number: ")
    login_unhandled(inp)