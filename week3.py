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

Every variable has a TYPE. The type of a variable tells you what kind of value it's storing.

We've seen a few types so far:
 
 - Integers: whole numbers
	You can convert variables to integers using int( )
	Examples: 1, 0, -14, 987654321

 - Float: fancy word for decimals, numbers with decimal points
	We haven't really seen floats before, but they behave similarly to integers
	You can convert variables to floats using float( )
	Examples: 1.414, 3.14, 2.5, -1729.42

 - Strings: text in quotes
 	You can convert variables to strings using str( )
	Examples: "bill nye", "1", "2 + 2 = 5", ""

 - Boolean: variables that can only take on the value of True or False
	You can convert variables to booleans using bool( )
	Examples: True, False (the only possible examples)

It's important to remember that you cannot mix and match types when doing stuff like addition.

For example, you can't do:
42 + "hello"	# Wrong!
2 + "2"			# Wrong!

We can convert "2" to an integer and then add:
2 + int("2")	# 4

However, there is ONE exception.
Python will automatically convert integers to floats when doing operations involving one integer and float.
So the following is valid:
2 + 3.14	# 5.14

These are only four types out of the many types in Python.
Let's look at another very useful type: Lists
'''

'''
# Lists are lists.
# They store several items as a list.
# Lists are ORDERED
# The items can be of any data type, even other lists.

# Here is an example of a list:

my_list = [1, "hello", True, 3.14, []]

# The square brackets [] tell you that this is a list.
# It contains the elements:
# 1, an integer
# "hello", a string
# True, a boolean
# 3.14, a float (decimal)
# [], an empty list
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
# This next section is very imporant!
# Pay close attention!

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

# We can also add an element to the end using .append()
shopping_list.append("pomegranate")
print(shopping_list)

# Or at any position using .insert()
# Inserts "doritos" before the SECOND item (index 1)
shopping_list.insert(1, "doritos")
print(shopping_list)

# We can also delete an item using .remove()
shopping_list.remove("pineapples")
print(shopping_list)
'''


'''
ACTIVITY 3: One at a time!

Ask the user for their name, age, and favorite animal. Add their answers to a list, and print it out!
'''


'''
ACTIVITY 4: Last!

Print the last element of the list you created in ACTIVITY 3.

How can you find the last element of any list?
'''


'''
ACTIVITY 5: Reversed 2

Create a list containing the first 10 positive integers in reverse order. Then print it out.

Can you do it with .append()? What about with .insert()?
'''


'''
# For loops and lists

# Consider a typical for loop:

# prints the numbers 0, 1, 2, ... 9
for i in range(0, 10):
	print(i)

# What if we want to do something with each element in a list?
# This is called ITERATING through the list

shopping_list = ["evaporated milk", "avocados", "pineapples"]

# It's actually quite easy
for item in shopping_list:
	# Do something interesting
	print(item)


# On a related note, what if we want to split a sentence string into a list of individual words?
# For example: "hello my name is Bob" -> ["hello", "my", "name", "is", "Bob"]

# We can use the function .split()
sentence = "hello my name is Bob"
word_list = sentence.split()

# Now we can iterate through the word_list!
for word in word_list:
	# Do something interesting
	print(word)
'''


'''
ACTIVITY 6: Factor

Ask the user to input a number, create a list containing all the factors of the number. Then find the sum of all the items in the list and print it out.

Hint: The % operator finds the remainder of a division. For example, 20 % 6 = 2 because 20 = 6 * 3 + 2, so 2 is the remainder.

Hint 2: What must the remainder be if another number is a factor of the input number?
'''



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



'''
REVIEW

We looked at another very useful data type today: lists.

Lists are extremely versatile and can even contain other lists as items.
Paired with for loops, they are even more powerful.

Note that in Python, the first item on the list has INDEX 0, the second has index 1, and so on. The last item has index len(your_list) - 1, or index -1 as shorthand.

We also looked at functions, which allow us to break up complicated tasks into smaller ones.
'''



'''
CHALLENGE 1: Todo

Simulate a todo list! Ask the user to input the action they want to do: append or remove. Then ask for what item to append or remove and print the list after every action!
'''



'''
CHALLENGE 2: 4-"function" calculator

Mimic a calculator, with operations as functions! Ask the user for a space separated math expression like "2 + 2" or "9 / 2". Then, use .split() to split the input string into three words, for example, ["2", "+", "2"] or ["9", "/", "2"]. Now write for functions for each operation and use the functions to evaluate the answer! Make sure you remember what the type of each variable is!
'''


