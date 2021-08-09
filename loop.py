# SUM of N numbers 
print('SUM OF n NUMBERS \n -----------------------')
n= int(input('Enter value of n (Limit 100)  :'))
sum=0
for i in range(0,n+1):
    sum +=i
print('Sum of ' + str(n)+ ' numbers is '+ str(sum))
# Even number Limit 20
print('Even numbers Limit 20 \n -----------------------')
for i in range(2,21):
    if i%2 == 0:
        print(i)

# Sum of Odd number b/w 0 tom 40
print('\nSum of odd numbers \n -----------------------')
sum = 0
for i in range(0,40):
    if i%2 != 0:
        sum+=i
print('Sum of odd number b/w 0 and 40 is : '+ str(sum))
