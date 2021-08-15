# # Question 1 Multi table of t2
# for i in range(1,11):
#     print(f'{i} x 2 = {i*2}')


# InPut=input('Enter Your input :')
# if InPut.isnumeric():
#     print(f' You Entered a Numeric  = {int(InPut)} ')
# else:
#     print('Input in lower case : ',InPut.lower())
#     print(f'Input in Upper case : {InPut.upper()}')
#     print(f'Input in Swap case : {InPut.swapcase()}')
#     print(f'I44nput in Capitalized  : {InPut.capitalize()}')
# test From macdf xclice



def myfn(**data):
    print(data)
    print(type(data['key1']))

myfn(key1='name',key2=2.3,Key3=3,key4=4,key5=5)
