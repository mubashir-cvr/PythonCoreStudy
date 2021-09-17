



# import sys
# nPerson = int(input('Number of person :'))
# persons =[]

# for i in range(0,nPerson):
#     person={
#         'Name':input(f'Name of person {i+1}:'),
#         'Age':input(f"Age person {i+1}:"),
#         'Phone':input(f'Phone of person {i+1}:')
#     }
#     print('-'*50)
#     persons.append(person)
# while True:
#     flag=0
#     search = input('Serach Person with Name/ Phone/ Age / Keywords :')
#     for p in persons:
#         for k,v in p.items():
#              if search.lower() in v.lower():
#                  flag=1
#                  print('-'*50)
#                  for k,v in p.items():
#                      print(k, ':' ,v)
#                  print('-'*50)
#     if flag==0:
#         print('Not Found')