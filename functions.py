# Argument type
def greet(name, msg):
    """This function greets to
    the person with the provided message"""
    print("Hello", name + ', ' + msg)

greet("Monica", "Good morning!")




# Default Argument type
def greetDefault(name, msg="Good morning!"):
    """
    This function greets to
    the person with the
    provided message.

    If the message is not provided,
    it defaults to "Good
    morning!"
    """

    print("Hello", name + ', ' + msg)


greetDefault("Kate")
greetDefault("Bruce", "How do you do?")



# Arbitrary Arguments
def greetArbitary(*names):
    """This function greets all
    the person in the names tuple."""

    # names is a tuple with arguments
    for name in names:
        print("Hello", name)


greetArbitary("Monica", "Luke", "Steve", "John")




#Arbitary Argumetn With Key,Value
def myfn(**data):
    print(data)

myfn(key1=1,key2=2,Key3=3,key4=4,key5=5)




# KeyWord Argument 
    # 2 keyword arguments
greet(name = "Bruce",msg = "How do you do?")

    # 2 keyword arguments (out of order)
greet(msg = "How do you do?",name = "Bruce") 

    # 1 positional, 1 keyword argument
greet("Bruce", msg = "How do you do?")  

