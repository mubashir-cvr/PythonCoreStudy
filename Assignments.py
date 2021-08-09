# # Question 1 Multi table of t2
# for i in range(1,11):
#     print(f'{i} x 2 = {i*2}')


InPut=input('Enter Your input :')
if InPut.isdecimal():
    print(f' You Entered a Decimal = {InPut} '.center(40,'#'))
else:
    print(f'Input in lower case : {InPut.lower()}')
    print(f'Input in Upper case : {InPut.upper()}')
    print(f'Input in Swap case : {InPut.swapcase()}')
    print(f'Input in Capitalized  : {InPut.capitalize()}')
