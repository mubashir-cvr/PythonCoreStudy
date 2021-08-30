from typing import List


lst =['R','G','B']
val=[200,255,200]

ziped = zip(lst,val)

# print(list(ziped))

#Unzip

color,value =zip(*ziped)

print(color)
print(value)