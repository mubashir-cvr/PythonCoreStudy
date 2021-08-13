import time

# print(dir(time))   # print methods in package
CurrentTime= time.localtime(time.time())
print('Formated Dtae and Time \n##############################')
print('\nCurrent Date YYYY/MM/DD:',CurrentTime[0],'/',CurrentTime[1],'/',CurrentTime[2])
print('Current Time Hr:Min:Sec:',CurrentTime[3],':',CurrentTime[4],':',CurrentTime[5])

print('Age Calculation \n##############################')
def agecalc(year):
    return CurrentTime[0]-year

dob=int(input('Enter Birth Year :'))
print('Age is :',agecalc(dob))

print('Weekday of Current date \n##############################')
if(CurrentTime[6]==0):
    print('Monday')
elif(CurrentTime[6]==1):
    print('Tuesday')
elif(CurrentTime[6]==2):
    print('Wednesday')
elif(CurrentTime[6]==3):
    print('Thursday')
elif(CurrentTime[6]==4):
    print('Friday')
elif(CurrentTime[6]==5):
    print('Saturday')
else:
    print('Sunday')

