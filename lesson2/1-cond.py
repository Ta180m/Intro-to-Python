'''
INTRODUCTION TO
    ______  __________  ______  _   __
   / __ \ \/ /_  __/ / / / __ \/ | / /
  / /_/ /\  / / / / /_/ / / / /  |/ / 
 / ____/ / / / / / __  / /_/ / /|  /  
/_/     /_/ /_/ /_/ /_/\____/_/ |_/   
                                      
CONDITIONALS

We make decisions every day, such as what to eat for lunch or what to wear. We make these decisions based on our knowledge and outside conditions, such as what's in the fridge or the weather outside.

How do computers make decisions? Let's look at some examples.
'''


# Let's say we have a variable called temperature which is the temperature outside.
# Based on the temperature, let's decide what to wear.

# current temperature is 20 degrees
temperature = 20

if temperature < 32:
	# it's really cold outside, what should I wear?
	# this code runs when the temperature is less than 32
	print("It's really cold, you should wear a: ")

# Here, temperature < 32 is a condition
# It can either be True or False
# 	If it is True, it will run the indented code below it
#   If it is False, it will NOT run the code and skip ahead

# VERY IMPORTANT: To indent, press the Tab key
# Python is really picky about indentation, so ALWAYS USE THE TAB KEY
# DO NOT TYPE 4 SPACES or Python will yell at you


# We can add an else case that runs when the condition is not true
if temperature < 32:
	# Runs when temperature is less than 32
	print("It's really cold outside, you should wear a: ")
else
	# Otherwise, when temperature is NOT less than 32
	# So temperature is greater of equal to 32
	# Run this code
	print("It's probably not that bad, you should wear a: ")


# We can use elif (else if) to add more cases
# Each case below must be indented using the tab key
if temperature < 32:
	# Runs when temperature less than 32
	print("really cold")
elif temperature <= 60: # <= means less than or equal to
	# Runs when temperature is NOT less than 32
	# So temperature is greater or equal to 32
	# And temperature is less than or equal to 60
	print("kind of cold")
else:
	# Runs otherwise, so temperature greater than 60
	print("not cold")


'''
Let's look at Activities 1, 2, and 3!
'''

# Type in the console:
temperature = 60
temperature < 32
temperature > 50

# Conditions are always True or False
# We can assign the value of a condition to a variable

cold_outside = temperature < 32
# cold_outside is a BOOLEAN variable
# Booleans are another type, like integers and strings
# They can only store the values True or False
# In this case, cold_outside is True if the temperature is less than 32
# and false otherwise

# Let's say the temperature falls
temperature = 20
temperature < 32
temperature > 50

cold_outside = temperature < 32


'''
Let's look at Activity 4 now!
'''

