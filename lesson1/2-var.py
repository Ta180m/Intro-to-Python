'''
INTRODUCTION TO
    ______  __________  ______  _   __
   / __ \ \/ /_  __/ / / / __ \/ | / /
  / /_/ /\  / / / / /_/ / / / /  |/ / 
 / ____/ / / / / / __  / /_/ / /|  /  
/_/     /_/ /_/ /_/ /_/\____/_/ |_/   
                                      
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


# Let's make a variable named age_of_Bob. This value will represent the age of Bob :).

age_of_Bob = 5
# We're doing 2 things in 1 line
# 1) We create a variable named age_of_Bob
# 2) We give the variable the value 5.

# ATTRIBUTES of the variable age_of_Bob
#      The variable NAME is age_of_Bob
#      The variable's VALUE is 5
#      The variable TYPE is Integer

# Variables names are CASE-SENSITIVE
# That means age, AGE, and Age are three different variables


# Let's create a new variable named age_of_Sally. Sally is twice as old as Bob.
# When you use a variable, Python substitutes the value of the variable in
age_of_Sally = age_of_Bob * 2
# We are doing 3 things above:
# 1) We are creating a new variable named age_of_Sally
# 2) We are calculating age_of_Bob * 2 (which is =10)
# 3) We are assigning 10 to the variable age_of_Sally
# Thus, age_of_Sally now has a value of 10


# It's Bob's birthday today!
# He is now 6 years old
# We can give the variable age_of_Bob a new value
# After all, it's just a memory "slot"
age_of_Bob = 6



'''
ACTIVITY 2: Experimenting with variables

Make a variable named my_age and give it the value of your actual age
Then, print the value 
'''



#  There are many types of variables
# age_of_Bob and age_of_Sally are INTEGER type variables
# There are also String, arrays, and other types of variables

your_name = "Bill Wender"
# The variable TYPE is String

# your_name = Bill Wender # WRONG
# When creating a String, make sure the value has quotations around it
# Otherwise, the computer will think Bill and Wender are variables

# print the value of your_name.
print("And your name is:")
print(your_name)

# we can change the value of your_name
your_name = "Bill Nye"

# Now it's "Bill Nye"
print("Now your name is:")
print(your_name)


# How do you tell the different between INTEGER and STRING types?
# Integers will be green
# Strings will be red with quotes

# the computer will compute the value
print(30 + (12 - 6) * 2)
# quotes indicate it is a String
print("30 + (12 - 6) * 2")
# without the quotes, computer will assume the text is a variable
print(your_name)


'''
ACTIVITY 3: What is wrong with this code?

Figure out what is wrong in the code below!
'''

'''
# name = "Bob" + 1

# Solution: the values must be the SAME TYPE.
# "Bob" is a string, while 1 is an integer
# It's like trying to add the number 7 to the word "tissue"

name = "Bob"
# new_name = "Bob" + 1

# Here, name is a string, and 1 is an integer
# So again, we cannot mix and match different types
'''

