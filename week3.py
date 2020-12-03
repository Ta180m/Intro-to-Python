'''
INTRODUCTION TO
    ______  __________  ______  _   __
   / __ \ \/ /_  __/ / / / __ \/ | / /
  / /_/ /\  / / / / /_/ / / / /  |/ / 
 / ____/ / / / / / __  / /_/ / /|  /  
/_/     /_/ /_/ /_/ /_/\____/_/ |_/   
                                      
WEEK 3

 - Data types

 - Functions


FOR STUDENTS:

 - Make sure you have an Repl.it account!

 - Click "Introduction-to-Python" at the top, then click the button "Fork"
 
 - This will create your own copy of the project.
 
 - After you have your own copy, click "Share" in the top right and send the link to your group leader.

 - Watch the group leader's shared screen during the examples, and work on your own copy for the activities!

'''


'''
DATA TYPES

We've seen a few types so far:
 
 - Integers: whole numbers
	You can convert variables to integers using int( )
	Examples: 1, 0, -14, 987654321

 - Float: fancy word for decimals, numbers with decimal points
	You can convert variables to floats using float( )
	Examples: 1.414, 3.14, 2.5, -1729.42

 - Strings: text in quotes
 	You can convert variables to strings using str( )
	Examples: "bill nye", "1", "2 + 2 = 5", ""

 - Boolean: variables that can only take on the value of True or False
	You can convert variables to booleans using bool( )
	Examples: True, False (the only possible examples)

However, there are much, much more types out there.
'''

'''
# Let's look at another very useful type: Lists

# Lists are lists.
# They store several items as a list.
# The items can be of any data type.

# Here is an example of a list:

my_list = [1, "hello", True, 3.14]

# The square brackets [] tell you that this is a list.
# It contains the elements:
# 1, an integer
# "hello", a string
# True, a boolean
# 3.14, a float (decimal)
# Additionally, we set the value of the variable my_list equal to this list

'''

'''
ACTIVITY 1: What's wrong?

What's wrong with my_list?

my_list = [2 + 2, "red", true]
'''



'''
ACTIVITY 2: Create your own!

Create your own list! It should be in the format [name, age, favorite animal]

After you create the list, print it!
'''


'''
# What can we do with lists?

# We can get the item at a certain position of the list!

# Let's say we have the following list:
shopping_list = ["evaporated milk", "avocados", "pineapples"]
print(shopping_list)

# To get the first element of the list, we use: shopping_list[0]
# [0] is not a mistake!
# In Python, the first element corresponds to INDEX 0
print("First element (index 0) is " + shopping_list[0])

# Or the second element: shopping_list[1]
# Second element corresponds to index 1
print("First element (index 1) is " + shopping_list[1])

# We can then modify the element
# Change "avocados" to "fruit roll-ups"
shopping_list[1] = "fruit roll-ups"
print(shopping_list)
print("First element (index 1) is " + shopping_list[1])

# We can also add an element to the end using append()
shopping_list.append("pomegranate")
print(shopping_list)

# Or at any position using insert()
# Inserts "doritos" before the SECOND item (index 1)
shopping_list.insert(1, "doritos")
print(shopping_list)

# We can also delete an item using remove()
shopping_list.remove("pineapples")
print(shopping_list)
'''


'''
ACTIVITY 3: One at a time!

Ask the user for their name, age, and favorite animal. Add their answers to a list, and print it out!
'''


'''
ACTIVITY 4: 

'''


'''
Is this necessary?

CASTING

Casting is used to convert values from one data type to another

int("5"), int(" 5  "), int(5.55), and int(5) all evaluate to 5
int(-1.6) evaluates to -1

float("3"), float(3), and float(3.0) all evaluate to 3.0

str(4) evaluates to "4"
str(4.2) evaluates to "4.2"
str("123") evaluates to "123"
str([1, 3.0]) evalutes to "[1, 3.0]"

bool(13), bool(-1.3), bool("sb2"), bool("False"), bool([1, 2]) all evaluate to True
bool(0), bool(0.0), bool(""), and bool([]) all evaluate to False

What if we tried: int("hello"), int("5.5")
'''




''''
FUNCTIONS

Think of functions as a mysterious cube that eats "input" and spits out "output".
(Also, it takes in "invisible" inputs and outputs. The inputs being pre-existing variables, and outputs = the changes made to those variables)

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
  -Will run 
  -But you aren't changing the value of a variable (thus no return statement)

# Let's say we "call" the function (aka use the function) with:
FirstNumber=5
SecondNumber=3
result = addNumbers(FirstNumber, SecondNumber)

# How are "number1" and "FirstNumber" different

***number1 and number2 are the NAMES of the input. They become variables, but don't affect the value of FirstNumber or SecondNumber***

'''


'''
ACTIVITY 5: Add 3

Create a function that takes in 3 integers and returns their sum!
'''

'''
Need to fix!

ACTIVITY 6: Find the difference!

They look similar, but why do they produce different output?
'''

'''
# 1)
def addToCount():
	count = count + 1
	print("count is now = " + count)

for i in range(5):
  addToCount()

# 2)
count = 5

def addToCount():
	count = count + 1
	print("count is now = " + count)

for i in range(5):
	addToCount()
'''

'''
ACTIVITY 7: 

'''


'''
REVIEW


'''


'''
CHALLENGE 1: Todo

Simulate a todo list!

'''


'''
CHALLENGE 2: 4-"function" calculator

Mimic a calculator, with operations as functions!
'''
