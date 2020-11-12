'''
INTRODUCTION TO
    ______  __________  ______  _   __
   / __ \ \/ /_  __/ / / / __ \/ | / /
  / /_/ /\  / / / / /_/ / / / /  |/ / 
 / ____/ / / / / / __  / /_/ / /|  /  
/_/     /_/ /_/ /_/ /_/\____/_/ |_/   
                                      
WEEK 1

 - Printing output
 
 - Variables
 
 - Reading input


Slides from last week:

https://docs.google.com/presentation/d/1FP5xCCzeM-IY8dQ1ZJNYqjy3RSc3YqrJ267_a-5nUmE/edit?usp=sharing
'''


'''
PRINTING OUTPUT

Let's get started with learning Python!
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
# It prints "Hello, world!" in the console
# The console is the black box on the right
# Press "Run" at the top to see it in action!
print("Hello, world!")

# Print some more text
print("Python is fun!")
print("this is a string")
# A string is some text enclosed in quotes

# note that the 4 doesn't have quotes
# it is an integer
print(4)

# Prints 4
print(2 + 2)

# Prints the LITERAL TEXT 2 + 2
print("2 + 2")

# Notice that strings and integers are two different things!
# They are different TYPES

# Each print puts the result on a new line
print("2 + 2 = ")
print(2 + 2)

# Prints a blank line
print()

'''
ACTIVITY 1: Print something fun!
Each member of the group should print their name, their age, and their favorite food.
'''



''''
VARIABLES

Just like you, computers have memory
We use variables to store information in the computer's memory
A variable is just a named "slot" in the computer's memory

Imagine a computer's memory being a huge warehouse of unlabeled boxes
Each box represents a potential variable
When you create a variable, you do 2 things
 1) You write the variable NAME on the side of the box
 2) You put the variable's VALUE INTO the box
 *all the unlabeled boxes are memory slots with no variable or value assigned
'''


# Let's make a variable named "age_of_Bob." This value will represent the age of Bob :).

age_of_Bob = 5
# We're doing 2 things in 1 line
# 1) We create a variable named "age_of_Bob"
# 2) We give the variable the value 5.

# ATTRIBUTES of the variable "age_of_Bob"
#      The variable NAME is "age_of_Bob"
#      The variable's VALUE is 5
#      The variable TYPE is Integer


# Let's create a new variable named "age_of_Sally." Sally is twice as old as Bob. 
age_of_Sally = age_of_Bob * 2
# We are doing 3 things above:
# 1) We are creating a new variable named "age_of_Sally"
# 2) We are calculating age_of_Bob * 2 (which is =10)
# 3) We are assigning 10 to the variable "age_of_Sally"
# Thus, age_of_Sally now has a value of 10


# It's Bob's birthday today!
# He is now 6 years old
# We can give the variable age_of_Bob a new value
# After all, it's just a memory "slot"
age_of_Bob = 6


'''
ACTIVITY 2: Experimenting with variables

Make a variable named "MyAge" and give it the value of your actual age
Then, print the value 
'''



#  There are many types of variables
# age_of_Bob and age_of_Sally are INTEGER type variables
# There are also String, arrays, and other types of variables

name = "Bill Wender"
# The variable TYPE is String
# When creating a String, make sure the value has quotations around it
# Otherwise, the computer will think "Bill" and "Wender" are variable names

# print the value of name.
print("And his name is:")
print(name)

# we can change the value of name
name = "Bill Nye"

# Now it's "Bill Nye"
print("Now his name is:")
print(name)


# How do you tell the different between INTEGER and STRING types?
# Integers will be green
# Strings will be orange with quotations

# the computer will compute the value
print(30+(12-6)*2)
# quotes indicate it is a String
print("hello I am a string")
# without the quotes, computer will assume the text is a variable
print(name)


'''
ACTIVITY 3: What is wrong with myVariable?

Figure out what is wrong in the code below!
'''

name = "Bob"
new_name = name + 1

# Solution: the variables must be the SAME TYPE.
# name is a string, while 1 is an integer
# It's like trying to add the number 7 to the word "tissue"



'''
READING INPUT

Let's say we want to find out what the user's name is. We can do that by using input()
It's quite easy once we see an exampple
'''

# Let's get some info about the user
print("What's your name?")

your_name = input() # type your name into the console

print("Your name is:")
print(your_name)


print("What's your age?")

your_age = input()

print("Your age is:")
print(your_age)

print("After your next birthday, you will be:")
print(your_age + 1)

# Whoa!
# input() gets input as a string
# So, your_age is a string
# And you can't add 1 to a string, as we saw earlier!

# So, what do we do?
print("Your age, as a string:")
print(your_age)

# We can use int(your_age) to CONVERT your_age from a string into an integer
print("Your age, as an integer:")
print(int(your_age))

# Now it works!
print("After your next birthday, you will be:")
print(int(your_age) + 1)


first_name = "Bill"
last_name = "Wender"

# When we "add" two strings, we mash them together to create a new string
# this called "concatenating" if you want to use the fancy word
name = first_name + last_name

print("His name is:")
print(name)

# Oops! That doesn't look right.
# Let's add a space in the middle
name = first_name + " " + last_name
print("This should be better:")
print(name)


'''
ACTIVITY 4: What's wrong with this code?

Figure out what's wrong here!
'''

ans = 5
print("2 + 2 = " + ans)



'''
ACTIVITY 5: Converting between strings and integers

Ask for the user's age, then ask them what age they think they will finish school
Print the number of years of school left for them!
'''



'''
REVIEW

Let's go over what we learned today
'''

# Variables have a NAME, a TYPE, and a VALUE

# You can't mix and match different types when doing addition
sum = 2 + 2 # OK
full_name = "Bill" + " " + "Wender" # OK
bad = "Bill" + 2 # ERROR


# Below will be a bunch of lines of code. This is for those who learn better visually.

my_age = 5
my_name = "Theo"
my_new_age = my_age + 1
print("hi")

# print("my name is")
# print(my_name)
print("my name is: " + my_name)



'''
CHALLENGE 1: Mad Libs

Want to go the extra mile? Try this challenge:


'''



'''
CHALLENGE 2:

Want to go the extra mile? Try this challenge:


'''

