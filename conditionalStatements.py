# Conditional if-else
d=int(input("Enter a number: "))
if d%2==0:
    print(str(d)+" is even number.")
else:
    print(str(d)+" is odd number")

#conditional operators and/&, or/|, not

# Conditional if-elif-else
if d%3==0 and d%5!=0:
    print(str(d)+" By 3")
elif d%5==0 and d%3!=0:
    print(str(d)+" By 5")
elif d%3==0 and d%5==0:
    print(str(d)+" Hello, world")
else:
    print(str(d)+" nothing")

n1 = 100
n2 = 100

print("N1") if n1 > n2 else print("=") if n1 == n2 else print("N2")

m= int(4)
# match m :
#     case 2: 
#         print("number 2.")
#     case _:
#         print("Other number")

# Ternary operator
age=22
price=20 if int(age)>=20 else 5
print(price)