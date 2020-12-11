'''
INTRODUCTION TO
    ______  __________  ______  _   __
   / __ \ \/ /_  __/ / / / __ \/ | / /
  / /_/ /\  / / / / /_/ / / / /  |/ / 
 / ____/ / / / / / __  / /_/ / /|  /  
/_/     /_/ /_/ /_/ /_/\____/_/ |_/   
                                      			
FUNCTIONS
'''


# Let's say we are going to be printing "Hello" and "World" a lot

print("Hello")
print("World")

print("abc")

print("Hello")
print("World")

print("123")

print("Hello")
print("World")


# Instead of writing 
print("Hello")
print("World")
# Three times, we can use a function:

def hello():
	print("Hello")
	print("World")

# Make sure you have a : colon after the parentheses!

# Now every time we use the function, Python will do
# print("Hello")
# print("World")

hello()
print("abc")
hello()
print("123")
hello()


'''
Let's do Activity 10 now!
'''


# Some functions take in inputs and give back an output
# Let's say we want to print 'Hello NAME' for multiple names
print("Hello Alice")
print("Hello Bob")
print("Hello Bob")

# Think of functions as a mysterious machine that eats "input" and spits out "output".

# If you give the function an input, it will give you an output.

# Scenario: We want to add 2 numbers and print their sum. 
# Instructors, type this into a new file.

def addNumbers(number1, number2):
	number3 = number1 + number2
	return number3

# What does the function mean?
# "def" tells us that the line is a function
# "addNumbers" is the name of a function. 
# "number1" and "number2" are the names of the input
# "return" will be explained later


# But how do we use this function/return?
# You can...
# 1) Set variable = to function
#	result = addNumbers(5,3)
#	***The value that is "returned" will be set to "result"
# 2) Call function 
#	addNumbers(5,3)
#	-Will run the function
#	-But you aren't changing the value of a variable


# Let's say we "call" the function (aka use the function) with:
first_number = 5
second_number = 3
result = addNumbers(first_number, second_number)
print(result)

# How are "number1" and "first_number" different?
# number1 and number2 are the NAMES of the input.
# They become variables to use inside the function, but don't affect the value of first_number or second_number!


'''
Let's do Activities 11 and 12 now!
'''

