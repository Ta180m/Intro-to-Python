'''
INTRODUCTION TO
    ______  __________  ______  _   __
   / __ \ \/ /_  __/ / / / __ \/ | / /
  / /_/ /\  / / / / /_/ / / / /  |/ / 
 / ____/ / / / / / __  / /_/ / /|  /  
/_/     /_/ /_/ /_/ /_/\____/_/ |_/   
                                      
LISTS

Lists are one of the most versatile and important types in Python.
Let's learn about them!
'''


# Lists are lists.
# They store several items as a list.
# Lists are ORDERED
# The items can be of any data type, even other lists.

# Here is an example of a list:
my_list = [1, 7, 2, 9]

# The square brackets [] tell you that this is a list.
# It contains the four integers, 1, 7, 2, 9
# We set the value of the variable my_list equal to this list
# Let's check out its type in the console!
type(my_list)


# Here is another list
my_list = [1, "hello", True, 3.14, [2, 3]]

# It contains the elements:
1 		# an integer
"hello"	# a string
True	# a boolean
3.14	# a float (decimal)
[2, 3]	# another list

# Let's check out its type in the console!
type(my_list)


'''
Let's look at Activity 4 now!
'''


# What can we do with lists?
# Group leaders: make sure you are doing examples in the console!
# You can type python in the console to start up an interactive Python session.
# You know you are in a PYTHON console when it shows the >>>
# Instead of the orange thing
# You can then type in code and Python will run it as you go


# Let's say we have this shopping list:
shopping_list = ["evaporated milk", "avocados", "pineapples"]

print(shopping_list)


# We can get the item at a certain position of the list!

# To get the first element of the list, we use: shopping_list[0]
# [0] is not a mistake!
# In Python, the first element corresponds to INDEX 0
print("First element (index 0) is " + shopping_list[0])

# The index is basically the position of the item, minus 1
# We access items on the list based on their INDEX, not their position
# This may seem weird, but there are reasons for doing this.

# Here's a helpful chart
# Index:		0				1			2
# 		["evaporated milk", "avocados", "pineapples"]


# To get the second element: shopping_list[1]
# Second element corresponds to index 1
print("Second element (index 1) is " + shopping_list[1])

# To get the third element: shopping_list[2]
# Third element corresponds to index 2
print("Third element (index 2) is " + shopping_list[2])


# We can also modify items
# Change the item with index 1, "avocados", to "fruit roll-ups"
shopping_list[1] = "fruit roll-ups"

print(shopping_list)
print("First element (index 1) is " + shopping_list[1])


'''
Now let's do Activities 5 and 6!
'''


# Let's say we have this shopping list:
shopping_list = ["evaporated milk", "avocados", "pineapples"]

print(shopping_list)


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
Let's take a look at Activities 7 and 8!
'''


# Lists are extremely useful when paired with for loops!

# What if we want to do something with each element in a list?
# This is called ITERATING through the list

shopping_list = ["evaporated milk", "avocados", "pineapples"]

# It's actually quite easy
for item in shopping_list:
	# Do something interesting
	print("Buy " + item)


# On a related note, what if we want to split a sentence string into a list of individual words?
# For example: "hello my name is Bobert" -> ["hello", "my", "name", "is", "Bobert"]
# We can use the function .split()
sentence = "Hello my name is Billiam"
word_list = sentence.split(" ")
print(word_list)

# Now we can iterate through the word_list!
for word in word_list:
	# Do something interesting
	print(word + " says hi")


'''
Let's look at Activities 9 and 10!
'''

