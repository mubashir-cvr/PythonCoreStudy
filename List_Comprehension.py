# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

# newlist = [x for x in fruits if "a" in x]

# print(newlist)

items=[]
inputs=["item","price","quantity"]
numbofitem=int(input('Number of Item :'))
for i in range(numbofitem):
    item={}
    for attr in inputs:
        item[attr]=input(f'{attr.capitalize()}  :')
    items.append(item)
print('Items')
print('#'*50)
print(items)

#List Comprehension
newlist = [x for x in items if 'apple' in x['item'].lower()] 
print('Filtered Items (Apple)')
print('#'*50)

print(newlist)
keys=('item','price')
print('Filtered Item price')
print('#'*50)
for item in newlist:
    # Dict Comprehension
    item_and_price ={x:item[x] for x in keys} 
    print(item_and_price)
