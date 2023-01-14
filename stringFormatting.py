# String format {}placeeholder
name="Menyichel"
age=23
gpa=3.93344337
print('My name is {:s} and {:d} years old and gpa {:6.2f}.'.format(name, age, gpa))

age1 = 22
txt = "My name is Menee, and I am {}"
print(txt.format(age1))

# String formatting using index
name="Menyichel"
age=23
gpa=3.93344337
statment="My name is {0} and I am{1} years old and gpa {2}."
print(statment.format(name, age, gpa))