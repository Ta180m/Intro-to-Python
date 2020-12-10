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
#   If it is True, it will run the indented code below it
#   If it is False, it will NOT run the code and skip ahead

cold_outside = temperature < 32
# cold_outside is a BOOLEAN variable
# Booleans are another type, like integers and strings
# They can only store the values True or False
# In this case, cold_outside is True if the temperature is less than 32
# and false otherwise

# Let's say the temperature rises
temperature = 50
if temperature >= 32:
	# now the temperature is greater or equal to 32, so it is no longer cold outside
	cold_outside = False

# We can also add an else statement
# If cold_outside is True, it runs the code under if
# If cold_outside is False, it runs the code under else
if cold_outside:
	# It's freezing outside!
	print("It's freezing outside, you should wear a: ")
else:
	# It's not that bad
	print("It's not that bad, you should wear a: ")



'''
ACTIVITY 1: It's hot outside!

Add another case for when the temperature is above 80 degrees.
'''

'''
temperature = 90

if temperature < 32:
	# It's freezing outside!
	print("It's freezing! You should wear a: ")
# Add a case when the temperature is greater than 80

'''


'''
ACTIVITY 2: Your age 2.0

ASK the user for their age, then tell them what stage of life (baby, kid, teenager, adult, etc) they are in right now.

Hint: Use input() and print()
'''



'''
ACTIVITY 3: Password

Ask the user to enter a password. If has a length less than 8 characters, tell them their password is insecure! Otherwise, tell them that they chose a good password.

Hint: use len(string_here) to get the length of a string
'''


