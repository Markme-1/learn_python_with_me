"""
Today I am startting a new journey to learn python so learn with me...
goal - 1 week
Date- 04/11/2022

"""

#python Indentation

"""
Indentation refers to the spaces at the beginning of a code line.

Where in other programming languages the indentation in code is for readability only, the indentation in Python is very important.

Python uses indentation to indicate a block of code.

"""
x= 5
if (x < 10):
    print("x is less than 10")
else:
    print("x is grater than 10")


#python comments

"""
in python # is used to create a comments.
in python three inverted commas used to crate a multiple line comments
comments usually used to explain python code.
comments used to make the code more readable

"""
#this is an single line comment
"""
this is 
an multiple line
comment
"""

#python variables

"""
in any programming language variable is used to store data in it.
python has no command to declare a variable 

"""
x =2
y= "python"
print(x)
print(y)

"""Variables do not need to be declared with any particular type,
 and can even change type after they have been set."""

x= 2 
x= "this is a string"
print(x)

"""If you want to specify the data type of a variable, this can be done with casting."""
x= int(3) #x will be an integer it's 3 here
y= str(5) #here y will be '5' a string
z= float(7) #here z will be 7.0 a float value

"""to see the data type of a variable we can use type() function"""
ver1= 5
ver2= "hello world"
ver3= 8.5

print(type(ver1))
print(type(ver2))
print(type(ver3))

"""single or double quotes is used to decleare a string in a variable"""
exmpl= "this is a string"
#is same as
exampl= 'this is a string'

"""variables names are case sensitive lower case a and upper case A is not same"""
a= "a veriable"
#is not same as
A="a different variable"

"""
A variable can have a short name (like x and y) or a more descriptive name (age, carname, total_volume). Rules for Python variables:
A variable name must start with a letter or the underscore character
A variable name cannot start with a number
A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
Variable names are case-sensitive (age, Age and AGE are three different variables)

"""
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"


