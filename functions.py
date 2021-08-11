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




# Pass by Reference 
def passByref(n):
    print(n)
    print(n[0])

lst = [1,2,3,5]
passByref(lst)



# Scope of variable  Fuction 
item = 'Apple'
my_var ='Value from out side of the function '
def display():
    global item
    item = 'Mango'
    my_var='Value from  the function '
    print('Printing Item from Inside of fxn : ',item)
    print('Printing my_var from Inside of fxn : ',my_var)

display()
print('Printing Item from outside fxn: ',item)
print('Printing my_var from outside fxn: ',my_var)




# Anonymous Or Lamda Function 
double = lambda x: x * 2

print(double(5))