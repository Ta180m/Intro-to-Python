'''
INTRODUCTION TO
    ______  __________  ______  _   __
   / __ \ \/ /_  __/ / / / __ \/ | / /
  / /_/ /\  / / / / /_/ / / / /  |/ / 
 / ____/ / / / / / __  / /_/ / /|  /  
/_/     /_/ /_/ /_/ /_/\____/_/ |_/   
                                      
LISTS

Let's look at another very useful type: Lists
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
Let's look at Activities 3 and 4!
'''


# REWRITE!!


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
Let's take a look at activities 5, 6, and 7!
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
Let's look at Activity 8!
'''

