''''
FUNCTIONS

Functions combine multiple instructions into one line
Scenario: We want to print 'Hello' and 'World' between prints

print("Hello")
print("World")
print("abc")
print("Hello")
print("World")
print("123")
print("Hello")
print("World")

Instead of writing 
  print("Hello")
  print("World")
three times, you could use a function

def hello():
  print("Hello")
  print("World")

hello()
print("abc")
hello()
print("123")
hello()

Some functions take in inputs and give back an output
Scenario: We want to print 'Hello NAME' for multiple names
print("Hello Alice")
print("Hello Bob")
print("Hello Bob")

Think of functions as a mysterious machine that eats "input" and spits out "output".
(Also, it has "invisible" inputs and outputs. Invisible inputs = pre-existing variables, invisible outputs = the changes made to those variables)

If you give the function an input, it will give you an output.

Scenario: We want to add 2 numbers and print their sum. 
# Instructors, type this into a new file.

def addNumbers(number1, number2):
	number3 = number1 + number2
	return number3

# What does the function mean?
"def" tells us that the line is a function
"addNumbers" is the name of a function. 
"number1" and "number2" are the names of the input
"return" : explain later


# But how do we use this function/return?
You can...
1) Set variable = to function
  result = addNumbers(5,3)
  ***The value that is "returned" will be set to "result"
2) Call function 
  addNumbers(5,3)
  -Will run the function
  -But you aren't changing the value of a variable (thus no return statement)

# Let's say we "call" the function (aka use the function) with:
first_number=5
second_number=3
result = addNumbers(first_number, second_number)

# How are "number1" and "first_number" different?

***number1 and number2 are the NAMES of the input. They become variables to use inside the function, but don't affect the value of first_number or second_number***

'''


'''
ACTIVITY 7: Add 3

Create a function that takes in 3 numbers and returns their sum!
'''


'''
ACTIVITY 8: Find the difference!

They look similar, but why do they produce different output?
'''

'''
# 1)
count = 0

def addToCount():
	count = count + 1
	print("count is now = " + count)

for i in range(5):
  addToCount()

# 2)
count = 0

def addToCount():
	global count
	count = count + 1
	print("count is now = " + count)

for i in range(5):
	addToCount()
'''


'''
ACTIVITY 9: Spammer 2

Make a function that prints "I love Python!" with no inputs or returns, and call it 100 times!
'''



