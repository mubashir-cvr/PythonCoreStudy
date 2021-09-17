Name ='Mubashir'
Phone = "9656248731"
age=18

assert len(Phone) == 10 and  Phone.isdigit(), 'Not a Phone Number'
assert len(Name) in range(3,9), 'Name Length not match'
assert age in range(18,30), 'Age Restriction'
