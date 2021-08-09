# String Reverse 

s = 'Hello World'
print(s.capitalize())
print(s[::-1])

#String methods
print('Number of ls :' + str(s.count('l',0,10)))  
# count ('substr',startIndex,EndIndex)
print(f'Input in lower case : {s.lower()}')
print(f'Input in Upper case : {s.upper()}')
print(f'Input in Swap case : {s.swapcase()}')
#String Format 
s= 'hi {0},Welcome to {1} programming'
print(s.format('User','Python'))

s= 'hi {},Welcome to {} programming'
print(s.format('User','Python'))

s= 'hi {name},Welcome to {lang} programming'
print(s.format(name='User',lang='Python'))

#String Format usinf f string 

name = 'Mubashir'
age = 22
s= f'Hello {name} , Age : {age}'

print(s)

print(s.isdecimal())