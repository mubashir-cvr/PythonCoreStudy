item = 'Apple'
def display():
    global item
    item = 'Mango'
    print('Printing Item from Inside of fxn : ',item)

display()
print('Printing Item from outside fxn: ',item)