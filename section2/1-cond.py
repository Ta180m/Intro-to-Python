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

print("Temperature is " + str(temperature))

if temperature < 32:
	print("It's really cold, you should wear a: ")

  # it's really cold outside, what should I wear?
	# this code runs when the temperature is less than 32

# Here, temperature < 32 is a condition
# It can either be True or False
# 	If it is True, it will run the indented code below it
#   If it is False, it will NOT run the code and skip ahead
# Remember to include a colon : after the condition!

# VERY IMPORTANT: To indent, press the Tab key
# Python is really picky about indentation, so ALWAYS USE THE TAB KEY
# Click the settings gear on the left, and make sure:
# Indent type is tabs
# Indent size is 4
# DO NOT TYPE 4 SPACES to indent or Python will yell at you


# We can add an else case that runs when the condition is not true
print("Temperature is " + str(temperature))

#temperature = 50
if temperature < 32:
	# Runs when temperature is less than 32
	print("It's really cold outside, you should wear a: ")
else:
	# Otherwise, when temperature is NOT less than 32
	# So temperature is greater of equal to 32
	# Run this code
	print("It's probably not that bad, you should wear a: ")


# We can use elif (else if) to add more cases
# Each case below must be indented using the tab key
print("Temperature is " + str(temperature))

#temperature = 65
if temperature < 32:
	# Runs when temperature less than 32
	print("really cold")
elif (60 <= temperature <= 80): # we can test if a variable is in a certain range
	# <= means less than or equal to
	# Runs when temperature is between 60 and 80, inclusive
	print("pretty nice")
else:
	# Runs otherwise
	print("no comment")


temperature = 60

# We can also check if two things are equal
if temperature == 70: # Use == double equals to check equality
	print("The temperature is perfect outside!")

# WRONG! This is an error!
# if temperature = 70: # Sets the value of temperature to 70
#	print("The temperature is perfect outside! Or is it?")


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

# Boolean variables are useful when we want to test multiple conditions
# For example, let's say it is nice outside if the temperature is between 60 and 80

# We can first set it to True
nice_outside = True
temperature = 50 # Try changing the temperature and see what happens

# If the temperature is too cold, set it to False
if temperature < 60:
	nice_outside = False

# If the temperature is too hot, set it to False
if temperature > 80:
	nice_outside = False

print("The temperature is " + str(temperature))
# We can use not to test if a boolean variable or conditional is not true
if not nice_outside:
	print("It's not nice outside.")
else:
	print("It's nice outside!")


# We can use and to test if two conditions are both True
age = 18
has_license = False
if age >= 16 and has_license == True:
    print("You are old enough and have a driver's license.")
    print("You can drive!")
else:
    print("You can't drive yet!")


'''
Let's look at Activities 4, 5, and 6 now!
'''



