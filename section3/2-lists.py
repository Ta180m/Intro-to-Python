'''
INTRODUCTION TO
    ______  __________  ______  _   __
   / __ \ \/ /_  __/ / / / __ \/ | / /
  / /_/ /\  / / / / /_/ / / / /  |/ / 
 / ____/ / / / / / __  / /_/ / /|  /  
/_/     /_/ /_/ /_/ /_/\____/_/ |_/   
                                      
LISTS
'''

'''
# Lists store several items in a single list.
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
ACTIVITY 2: Create your own!

Create your own list! It should be in the format [name, age, favorite animal]

After you create the list, print it!
'''


# Let's say we have the following list:
shopping_list = ["milk", "avocados", "pineapples"]
print(shopping_list)

# To get the first element of the list, we use: shopping_list[0]
# [0] is not a mistake!
# In Python, the first element corresponds to INDEX 0
print("First element (index 0) is " + shopping_list[0])

# Or the second element: shopping_list[1]
# Second element corresponds to index 1
print("Second element (index 1) is " + shopping_list[1])

# We can then modify the element
# Change "avocados" to "fruit roll-ups"
shopping_list[1] = "fruit roll-ups"
print(shopping_list)
#print("First element (index 1) is " + shopping_list[1])

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
ACTIVITY 4: Last!

Print the last element of shopping_list.

How can you find the last element of any list?
Hint: len(my_list) gives the length of a list
'''




'''
ACTIVITY 5: Reversed 2

Create a list containing the first 10 positive integers in reverse order using a FOR LOOP. [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
Then print it out.

Can you do it with .append()? What about with .insert()?
'''
reverse_list=[]




# What if we want to do something with each element in a list?
# This is called ITERATING through the list

shopping_list = ["milk", "avocados", "pineapples"]

# It's actually quite easy
for item in shopping_list:
	# Do something interesting
	print("Buy",item)

# Iterating through a list is similar to a classic for loop
#for i in range(5):
#for i in [0, 1, 2, 3, 4]:





# On a related note, what if we want to split a sentence string into a list of individual words?
# For example: "hello my name is Bob" -> ["hello", "my", "name", "is", "Bob"]
# We can use the function .split()
sentence = "hello abc abab cat"
word_list = sentence.split(" ")
print(word_list)

# Now we can iterate through the word_list!
for word in word_list:
	# Do something interesting
	print(word+"hi")
