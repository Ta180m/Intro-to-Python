'''
INTRODUCTION TO
    ______  __________  ______  _   __
   / __ \ \/ /_  __/ / / / __ \/ | / /
  / /_/ /\  / / / / /_/ / / / /  |/ / 
 / ____/ / / / / / __  / /_/ / /|  /  
/_/     /_/ /_/ /_/ /_/\____/_/ |_/   
                                      
DATA TYPES

Every variable has a TYPE. The type of a variable tells you what kind of value it's storing.
'''

# We've seen a few types so far:

# INTEGERS: whole numbers
# You can convert variables to integers using int( )
int1 = 1
int2 = 0
int3 = -13
int4 = 987654321

# STRINGS: text in quotes
# You can convert variables to strings using str( )
str1 = "bill nye"
str2 = "1"
str3 = "2 + 2 = 5"
str4 = "" # empty string that contains no text

# BOOLEANS: variables that can only take on the value of True or False
# You can convert variables to booleans using bool( )
bool1 = True
bool2 = False
# the only possible examples

# It's important to remember that you CANNOT mix and match types when doing stuff like addition.

# For example, you can't do:
#42 + "hello"	# Wrong!
#2 + "2"			# Wrong!

# Recall that 2 and "2" are COMPLETELY DIFFERENT
# 2 is an integer while "2" is a string
# We can convert "2" to an integer and then add:
2 + int("2")	# 4


'''
Let's look at Activity 1!
'''


# Recall that integers are whole numbers
# What about decimals?

my_decimal = 3.14
print(type(my_decimal))

# Decimals are called FLOATS in Python
# We haven't seen floats before, but they behave similarly to integers
# You can convert variables to floats using float( )
# Examples of floats:
float1 = 1.414
float2 = 3.14
float3 = 2.5
float4 = -1729.42


# Remember how I said you can't mix and match types when doing addition?
# There is ONE exception.
# Python will automatically convert integers to floats when doing operations involving one integer and float.
# So the following is valid:
2 + 3.14 # 5.14


'''
Let's work on Activity 2!
'''

