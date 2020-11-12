'''
Introduction to Python

Week 1

 - Printing output
 
 - Variables
 
 - Reading input

'''


'''
Slides from last week:

https://docs.google.com/presentation/d/1FP5xCCzeM-IY8dQ1ZJNYqjy3RSc3YqrJ267_a-5nUmE/edit?usp=sharing
'''


'''
PRINTING OUTPUT
'''

# This is a comment
# It doesn't do anything

# A multiple-line comment
'''
Your first podcast will be awful
Your first video will be awful
Your first article will be awful
Your first art will be awful
Your first photo will be awful
Your first game will be awful
But your first code will be perfect.
Zero bugs and very clean code.
It will be "Hello, world!"
'''

# Your first program
# Prints "Hello, world!" in the console
# The console is the black box on the right
# Press "Run" at the top to see it in action!
print("Hello, world!")
# The above line is a "command". It tells the computer to do something

# Print some more text
print("this is a string")

# note that the 4 doesn't have quotes
# it is an integer
print(4)

# Prints 4 in the "console"
print(2 + 2)

# Prints the LITERAL TEXT 2 + 2
print("2 + 2")


'''
ACTIVITY 1: Print something fun!

'''



''''
VARIABLES

# Just like you, computers have memory
# We use variables to store information in the computer's memory
# A variable is just a named "slot" in the computer's memory

# Imagine a computer's memory being a huge warehouse of unlabeled boxes
# Each box represents a potential variable
# When you create a variable, you do 2 things
#  1) You write the variable NAME on the side of the box
#  2) You put the variable's VALUE INTO the box
# *all the unlabeled boxes are memory slots with no variable or value assigned
'''

# Let's make a variable named "ageOfBob." This value will represent the age of Bob :).

ageOfBob = 5
# We're doing 2 things in 1 line
# 1) We create a variable named "ageOfBob"
# 2) We give the variable the value 5.

# ATTRIBUTES of the variable "ageOfBob"
#      The variable NAME is "ageOfBob"
#      The variable's VALUE is 5
#      The variable TYPE is Integer


# Let's create a new variable named "ageOfSally." Sally is twice as old as Bob. 
ageOfSally = ageOfBob * 2
# We are doing 3 things above:
# 1) We are creating a new variable named "ageOfSally"
# 2) We are calculating ageOfBob * 2 (which is =10)
# 3) We are assigning 10 to the variable "ageOfSally"
# Thus, ageOfSally now has a value of 10


# It's Bob's birthday today!
# He is now 6 years old
# We can give the variable ageOfBob a new value
# After all, it's just a memory "slot"
ageOfBob = 6

'''
ACTIVITY 2
Make a variable named "MyAge" and give it the value of your actual age
Then, print the value 
'''




#  There are many types of variables
# ageOfBob and ageOfSally are INTEGER type variables
# There are also String, arrays, and other types of variables

name = "Bill Wender"
# The variable TYPE is String
# When creating a String, make sure the value has quotations around it
# Otherwise, the computer will think "Bill" and "Wender" are variable names

# print the value of name. 
print(name)

# we can change the value of name
name = "Bill Nye"

# Now it's "Bill Nye"
print(name)

#How do you tell the different between INTEGER and STRING types?
#Integers will be green
#Strings will be orange with quotations

print(5+5-(6*2)) # the computer will compute the value
print("aos8d7fhw") # " " indicate it is a String
print(ageOfBob) # without the " ", computer will assume the text is a variable


'''
ACTIVITY 3: WHAT IS WRONG WITH myVariable
'''

BobName = "Bob"
# myVariable = Bob + ageOfBob
# Solution: the variables must be the SAME TYPE.
# It's like you're trying to add the number 7 to the word "tissue"


'''
READING INPUT
'''

# Let's say we want to find out what the user's name is. We can do that by using the input() function
# It's quite easy once we see an exampple

print("What's your name?")

yourName = input()

print("Your name is:")
print(yourName)


print("What's your age?")

yourAge = input()

print("Your age is:")
print(yourAge)

print("After your next birthday, you will be:")
print(yourAge + 1)


'''
ACTIVITY 4

'''



'''
ACTIVITY 5

'''



'''
REVIEW
'''
#Below will be a bunch of lines of code. This is for those who learn better visually.

myAge = 5
myName = "Theo"
myNewAge = myAge + 1
print("hi")

#print("my name is")
#print(myName)
print("my name is: " + myName)


'''
MINI-PROJECT


'''
# Mini-project here(maybe have them make a madlibs type thing?)