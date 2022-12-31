def printt():
    print("Hello, World")
printt()

#single line comment
'''this is
   multi-comment
   line
'''
"""this comment 
   is also possible"""
#key words

#variable
x,y,z="orange",5,6.5
a=b=c="1",5
print(a,b,c)
print(x)
print(ord("c"))

print(type(x))#print data type of "x"

str1="Hello"
print(len(str1))

#recieving input
x=(input("Enter your name?"))
print("Hello "+x)
g=int((input("Enter first number?")))
h=int((input("Enter second number?")))
print("The sum is "+str(g+h))

print(print("c"))

#string format 
name="Menyichel"
age=23
gpa=3.93344337
print('My name is {:s} and {:d} years old and gpa {:6.2f}.'.format(name, age, gpa))

#access strings from string
name1="Dawit"
print(name1[0])
print(name1[-1])
print(name1[0:2]) #slicing

#string methods
print(name1.lower())

v="hello, world"
print(v.split(','))
print(v.replace("hello","HELLO"))

#type casting
cast="A"
print(bin(65))
print(oct(65))
print(hex(65))
print(str(65))

#conditional if-else
d=int(input("Enter a number: "))
if d%2==0:
    print(str(d)+" is even number.")
else:
    print(str(d)+" is odd number")

#conditional operators and/&, or/|, not

#conditional if-elif-else
if d%3==0 and d%5!=0:
    print(str(d)+" Hello")
elif d%5==0 and d%3!=0:
    print(str(d)+" Hello")
elif d%3==0 and d%5==0:
    print(str(d)+" Hello, world")
else:
    print(str(d)+" nothing")

m= int(4)
# match m :
#     case 2: 
#         print("number 2.")
#     case _:
#         print("Other number")

#ternary operator
age=22
price=20 if int(age)>=20 else 5
print(price)

#for loop
j=[1,2,3]
for jj in j:
    print(jj)
for i in range(0,10,2):
  print(i)
