"""
astr = "hello bob"
try:
    istr = int(astr)
except:
    istr = -1
print("First", istr)

astr = "123"
try:
    istr = int(astr)
except:
    istr = -2
print("Second", istr)



print("'------------")

rawstr = input("Enter a number:")
try:
    ival = int(rawstr)
except:
    ival = -1

if ival > 0 :
    print("nice work!")
else:
    print("not a number")
print("'------------")

big = max('Hello world','la;jdjaie','zzzZZZZZZZZ')
print(big)
import platform

x = dir(platform)
print(x)
"""
#import module
#module.ex()
#module.greeting("Bob")
#print(module.person1['age'])
#print(dir(module.person1))

"""
x, y, z = "Orange", "Banana", "Cherry"
print(x+y+z)
print(y)
print(z)

x = y = z = "Orange"
print(x)
print(y)
print(z)

fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)
print("----------------")
print(fruits)

x = "Python"
y = "is"
z = "awesome"
print(x, y, z)
print(x + y + z)
print("----------------")

x = 5
y = "John"
print(x, y)
"""

"""
x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

a = myfunc()

print("I say ", a)
#print(myfunc())



x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)

"""
"""

x = 1    # int
y = 2.8  # float
z = 1j   # complex

#convert from int to float:
a = float(x)

#convert from float to int:
b = int(y)

#convert from int to complex:
c = complex(3)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))

thislist = ["apple", "banana", "cherry"]
thislist[1] = "mango"
print(thislist)
print("\n")
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)
print("\n")
  
thislist = ["apple", "banana", "cherry"]
thislist.insert(1,"orange")
#print(thislist.pop(0))
del thislist[0]
print(thislist)
thislist.clear()
print(thislist)
print(len(thislist))


list1 = ["apple", "orange", "banana", "cherry"]
#list1.insert(-1, "huanggua")
list2 = [1, 2, 3]
newList = []

min_length = min(len(list1), len(list2))
for i in range(min_length):
    newList.append(list1[i] + str(list2[i]))
    list1[i] = newList[i]
print(list1)

thistuple = tuple(("apple", "banana", "cherry"))
print(list(thistuple))
print("\n")

thisset = {"apple", "banana", "cherry"}

x = thisset.pop()

print(x)

print(thisset)


print("\n"+"------------------")

thisset = {"apple", "banana", "cherry"}

thisset.clear()

print(thisset)

print("\n"+"------------------")


set1 = {"a", "b" , "c", 1}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)

print("\n"+"******************")


x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.intersection(y) 
x.intersection_update(y)
print(x)
print(z)



x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "facebook"}

z = x.isdisjoint(y) 

print(z)

x1 = {"apple", "banana", "cherry"}
y1 = {"google", "microsoft", "apple"}

z1 = x1.isdisjoint(y1) 

print(z1)
"""



"""
thisdict =	{
  "brand": "Porsche",
  "model": "911",
  "year": 1963
}
thisdict["year"] = 2019
thisdict["color"] = "red"

#print(thisdict)
for x in thisdict:
   # print(x)
    print(x + str(thisdict[x]))

print("\n"+"------------------")
thisdict.popitem()

for x, y in thisdict.items():
    print(x, y)
    
    
print("\n"+"------------------")

#thisdict.clear()
#print(thisdict) 


myfamily = {
  "child1" : {
    "name" : "Phoebe Adele",
    "year" : 2002
  },
  "child2" : {
    "name" : "Jennifer Katharine",
    "year" : 1996
  },
  "child3" : {
    "name" : "Rory John",
    "year" : 1999
  }
}

myfamily1 = {
  "child11" : {
    "name" : "aaaaa",
    "year" : 3002
  },
  "child22" : {
    "name" : "bbbbb",
    "year" : 3996
  },
  "child33" : {
    "name" : "ccccc",
    "year" : 3999
  }
}

ohmy = {
     "myfamily" : myfamily,
    "myfamily1" : myfamily1
}
print(ohmy)


child1 = {
  "name" : "Phoebe Adele",
  "year" : 2002
}
child2 = {
  "name" : "Jennifer Katharine",
  "year" : 1996
}
child3 = {
  "name" : "Rory John",
  "year" : 1999
}

myfamily = {
    "child1" : child1,
    "child2" : child2,
    "child3" : child3
}

print(myfamily)
print(len(myfamily))

print("\n"+"------------------")

thisdict = dict(brand="Porsche", model="911", year=1963)
# 请注意，关键字不是字符串字面量
# 请注意，使用了等号而不是冒号来赋值
print(type(thisdict))
print("\n"+"---------below is if else---------")


i = 1
while i < 6:
    i += 1
    print(i)

else:
  print("i is no longer less than 6")
  
  
  
print("\n"+"---------below is for---------")

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
for y in "fruits":
    if y == "u":
        break
    print(y)
    
    
print("\n"+"---------below is for---------")

for x in range(1, 10, 2):
    print(x)
    
    
print("\n"+"---------below is python函数---------")

def my_function(*kids):
    print("The youngest child is " + str(kids))
    print(str(kids))
#my_function("Phoebe", "Jennifer", "Rory")
thistyple = "Phoebe"
my_function(thistyple)



print("\n"+"---------below is python递归函数 K一直加到0---------")

def tri_recursion1(k):
    if(k > 0):
        result = k + tri_recursion(k - 1)
       # print(result)
    else:
        result = 0
    return result

print(tri_recursion1(2))

print("\n"+"---------below is python递归函数 阶乘---------")

def tri_recursion(k):
    if(k > 0):
        result = k * tri_recursion(k - 1)
       # print(result)
    else:
        result = 1
    return result

print(tri_recursion(4))
"""

