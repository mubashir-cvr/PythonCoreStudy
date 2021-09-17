# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

# newlist = [x for x in fruits if "a" in x]

# print(newlist)

# items=[]
# inputs=["item","price","quantity"]
# numbofitem=int(input('Number of Item :'))
# for i in range(numbofitem):
#     item={}
#     for attr in inputs:
#         item[attr]=input(f'{attr.capitalize()}  :')
#     items.append(item)
# print('Items')
# print('#'*50)
# print(items)

# #List Comprehension
# newlist = [x for x in items if 'apple' in x['item'].lower()] 
# print('Filtered Items (Apple)')
# print('#'*50)

# print(newlist)
# keys=('item','price')
# print('Filtered Item price')
# print('#'*50)
# for item in newlist:
#     # Dict Comprehension
#     item_and_price ={x:item[x] for x in keys} 
#     print(item_and_price)




#########################################

# lst =['Red','Green','Blue']
# _dst={k:[input('%s :'%v) for v in lst] for k in range(2)}

# print(_dst)

# _lst = {v for k,v in _dst.items() }

# print(_lst)

matrix = [[input(f'Enter {i},{j} th value :') for j in range(2)] for i in range(2)]
print('Martis :',end=" ") 
print(matrix)

