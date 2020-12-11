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
# The TYPE of the variable is VERY IMPORTANT
# Always make sure you know the type of your variables
# If you're not sure, you can get the type like this:
type(age_of_Bob)


# Variables names are CASE-SENSITIVE
# That means age, AGE, and Age are three different variables


# Let's create a new variable named age_of_Billiam. Billiam is twice as old as Bob.
# When you use a variable, Python substitutes the value of the variable in
age_of_Billiam = age_of_Bob * 2
# We are doing 3 things above:
# 1) We are creating a new variable named age_of_Billiam
# 2) We are calculating age_of_Bob * 2 (which is =10)
# 3) We are assigning 10 to the variable age_of_Billiam
# Thus, age_of_Billiam now has a value of 10

# Let's check that it has type of integer
type(age_Billiam)


# It's Bob's birthday today!
# He is now 6 years old
# We can give the variable age_of_Bob a new value
# After all, it's just a memory "slot"
age_of_Bob = 6



'''
Let's do Activity 3 now!
'''


# There are many differnet types of variables
# age_of_Bob and age_of_Billiam are INTEGER type variables since they are storing whole numbers
# Let's look at another type:

# Recall we can print text with quotes
print("Bill Wender")
# What we are really doing is making a STRING and printing the string out
# A STRING IS TEXT IN QUOTES

# We can also make a string and assign it to a variable
your_name = "Bill Wender"
# Now your_name has TYPE of STRING
# And contains the value "Bill Wender"

# your_name = Bill Wender # WRONG
# When creating a string, make sure the value has quotes around it
# Otherwise, Python will think Bill and Wender are variables

# print the value of your_name
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
# You can also use type( ) to get the type of a variable

# the computer will compute the value
print(30 + (12 - 6) * 2)
# quotes indicate it is a String
print("30 + (12 - 6) * 2")
# without the quotes, computer will assume the text is a variable
print(your_name)


'''
Now let's work on Activities 4, 5, and 6!
'''

