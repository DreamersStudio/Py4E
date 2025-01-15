"""
#a = 
"Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
#ut labore et dolore magna aliqua.""
"
print(a)

a = "Hello, World!"
#print(a[5])

#for x in a:
for x in "banana":
  print(x)

print(len(a))

txt = "The best things in life are free!"
print("free" in txt) #true or false

if "free" in txt:
  print("Yes, 'free' is present.")

txt = "The best things in life are free!"
print("expensive" not in txt)

txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")
  



age = 36
txt = f"My name is John, I am {age}"
print(txt)
price = 59
txt = f"The price is {price} dollars"
print(txt)
price = 59
txt = f"The price is {price:.5f} dollars"
print(txt)

txt = f"The price is {20 * 59} dollars"
print(txt)
print(txt)
txt = "We are the so-called \"Vikings\" from the north."
print(txt)

txt = "We are the so-called \'Vikings\" from the north."
print(txt)
txt = "We are the so-called \\Vikings\" from the north."
print(txt)
txt = "We are the so-called \nVikings\" from the north."
print(txt)


txt1 = "helloworld\rokay"
print("txt1 is \n"+txt1.upper()) 
txt = "aaaaHelloWorld!"
print(txt.capitalize())


txt1 = "hello world okay"
#print("txt1 is \n\n\n\n\n\r"+txt1.upper()) 
txt = "apple!"
#print(txt.capitalize())
#print(txt.casefold())
print(txt.center(20, "-"))

#txt = "banana"

#x = txt.center(20, "O")

#print(txt.center(20, "-"))
"""


#count()

txt = "I love apples, apple are my favorite fruit"

x = txt.count("apple")

print(x)

txt = "I love apples, apple are my favorite fruit"

x = txt.count("apple", 10, 24)

print(x)

#encode()
txt = "My name is Ståle"

x = txt.encode()

print(x,"\n\n\n\nBelow is more examples of encode()")



txt = "My name is Ståle"

print(txt.encode(encoding="ascii",errors="backslashreplace"))
print(txt.encode(encoding="ascii",errors="ignore"))
print(txt.encode(encoding="ascii",errors="namereplace"))
print(txt.encode(encoding="ascii",errors="replace"))
print(txt.encode(encoding="ascii",errors="xmlcharrefreplace"))



print("\n\n\n\nBelow is endswith()")

txt = "Hello, welcome to my world."
x = txt.endswith(".")
print(x)

txt = "Hello, welcome to my world."
x = txt.endswith("my world.")
print(x)

txt = "Hello, welcome to my world."
x = txt.endswith("my world.", 5, 11)
print(x)

txt = "Hello, welcome to my castle."
x = txt.endswith(("world.", "castle."))
print(x)

print("\n\n\n\nBelow is find()")


txt = "Hello, welcome to my world."

print(txt.find("q"))
print(txt.index(","))

print("------------\nBelow is format(value)\n------------")

#named indexes:
txt1 = "My name is {fname}, I'm {age}".format(fname = "Bill", age = 63)
#numbered indexes:
txt2 = "My name is {0}, I'm {1}".format("Bill",63)
#empty placeholders:
txt3 = "My name is {}, I'm {}".format("Bill",63)

print(txt1)
print(txt2)
print(txt3)

print("------------\nBelow is format(value)\n------------")



txt = "一二三"
x = txt.isdigit() #false
y = txt.isnumeric() #true
print(x,y)

txt = "一二三4"
x = txt.isdigit()   #false
y = txt.isnumeric() #true
print(x,y)

