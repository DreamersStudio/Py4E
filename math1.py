"""
x = 5
while x > 0 :
 print(x)
 x = x - 1
print("now x is ") 
print(x)



print("*************")

x = 5
if x < 2 :
    print('below 2')
elif x < 20 :
    print('below 20')
elif x < 10 :
    print('below 10')

else :
    print('done')

x = 2/3+1
print(x)
x = int(x)
print(x)
print(type(x))


import sys

print(sys.version)



n = 0
while True:
    if n == 3:
        break
    print(n)
    n = n + 1
    
    
if 5 > 2:
    print("Five is greater than two!")
else:
    if 2<3:    
        print("Five is greater than two!")
        
x = 1
print(type(x))
"""


import random

i = random.randrange(1, 10)
a = 0
print(i)
#i = 1
while i < 8:
  a += 1
  print(i,"run the",a,"time")
  i = random.randrange(1, 10)
else:
  print("-------", a)
  print(i," is no longer less than 8")
print("total run",a,"times")