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

Make sure you have an Repl.it account!
Click "Introduction-to-Python" at the top, then click the button "Fork"
This will create your own copy of the project.
Watch the team leader's shared screen during the examples, and work on your own copy for the activities!
'''


'''
DATA TYPES

We've seen a few types so far:
 
 - int: whole numbers
	Examples: 1, 0, -14, 237568178935

 - str: strings of text in quotes
	Examples: "bill nye", "1", "2 + 2 = 5", ""

 - bool: variables that can only take on the value of True or False
	Examples: True, False (the only possible examples)


However, there are much, much more types out there.

Let's look at another very useful type: Lists

Lists (list) are multiple values stored in a list
List items can be of any data type
We use brackets [] to represent lists
Examples: [1, 2.3, 5], ["red"], []

'''

'''
MORE ON LISTS

How do we define a list?

Like any variable, the name goes on the left and the contents go on the right.
'''

example_list = [1, 3, 2, 5]

'''
OPERATIONS ON A LIST

ADDITION

DELETION

PRINTING

'''

'''
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


'''
ACTIVITY 1: What's wrong?

What's wrong with this list?

this_list = [1, "red", true]

(there's nothing wrong)
'''

'''
ACTIVITY 2: Create own!

Create your own list!

It should be in the format [name, age, ?]

After you create the list, print it!

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
ACTIVITY 5: Add 3!

Create a function that takes in 3 integers and returns their sum!
'''

'''
ACTIVITY 6: Find the difference!
#Please copy part 1 into a new file, then delete and copy part 2

1)
count = 5

def addToCount():
  count = count + 1
  print("count is now = " + count)

for i in range(5):
  addToCount()

2)
def addToCount():
  count = count + 1
  print("count is now = " + count)

for i in range(5):
  addToCount()
'''


# Potential Activity: Mimic a calculator (with operations as functions, ask user for input numbers)
