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