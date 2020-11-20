'''
INTRODUCTION TO
    ______  __________  ______  _   __
   / __ \ \/ /_  __/ / / / __ \/ | / /
  / /_/ /\  / / / / /_/ / / / /  |/ / 
 / ____/ / / / / / __  / /_/ / /|  /  
/_/     /_/ /_/ /_/ /_/\____/_/ |_/   
                                      
WEEK 2

 - Conditionals: if, else, elif
 
 - Repetition: for, while

Don't worry if your group is a little bit behind. You'll get to the fun tic-tac-toe game next week!
'''



'''
CONDITIONALS

We make decisions every day, such as what to eat for lunch or what to wear. We make these decisions based on our knowledge and outside conditions, such as what's in the fridge or the weather outside.

How do computers make decisions? Let's look at some examples.
'''


'''
# Let's say we have a variable called temperature which is the temperature outside.
# Based on the temperature, let's decide what to wear.

# current temperature is 20 degrees
temperature = 20

if temperature < 32:
	# it's really cold outside, what should I wear?
	print("It's really cold, you should wear a: ")


# Here, temperature < 32 is a condition
# It can either be True or False
#   If it is True, it will run the code below it
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



'''
REPETITION

The world is full of repetition: you sleep and wake up every day, scientists repeat experiments many times to confirm their results, and history repeats itself (Read https://en.wikipedia.org/wiki/Historic_recurrence#Similarities if you don't believe me)

Computers were originally invented to automate computation, so they are also full of repetition. Let's see how we can use repetition in programs.
'''


'''
# Let's say we want to print the numbers 1 through 10

# We could do this:
print(1)
print(2)
print(3)
print(4)
print(5)
print(6)
print(7)
print(8)
print(9)
print(10)

# But what if we want to print the numbers from 1 to 100?
# That's a lot of work!

# We can use a FOR loop
for i in range(1, 11):
	print(i)

# What does this do?
# It will repeat for every i in the range 1 to 11
# We need to use 11 because 11 is NOT included
# So it will repeat for i = 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
'''


'''
ACTIVITY 4: Reversed!

Print the numbers from 1 to 10 in reverse order!

Hint: Instead of print(i), what else could we do?
'''



'''
ACTIVITY 5: Sum

Ask the user for a number n, and print the sum of the first n positive integers, basically, print 1+2+3+...+n
'''


'''
# However, sometimes we don't know how many times we want to repeat something
# Maybe we just want to repeat until a certain condition is satisfied
# We can use a WHILE loop

# maybe a better example, where the number of repetitions is not know?

day_of_week = 1 #monday is day 1
weekend = 6 #saturday is day 6

while (day_of_week < weekend):
  print("It is day " + day_of_week + ". Thus, it is not weekend yet")

print("It is day " + day_of_week + ". Thus, it IS the weekend")
'''



'''
ACTIVITY 6: Exponential growth

A rabbit population starts out with 2 rabbits. Each year, the population size doubles. Find the number of years before the population reaches 1000 using a while loop!
'''



'''
ACTIVITY 7: Password 2.0

Let's say the user's password is "ilovepython". Ask them to enter their password until they get it right.
'''



'''
ACTIVITY 8: Infinite loop

What happens when the following code runs? How can we fix it?
'''

'''
num_rabbits = 2
years = 0
while num_rabbits > 0:
	num_rabbits = 2 * num_rabbits
	years = years + 1
print(years)
'''


'''
REVIEW
'''


'''
# Today, we learned two important building blocks for making more sophisticated programs: CONDITIONALS and REPETITION


# We use if/elif/else so the computer can make decisions

language = "python"
if language == "python":
	print("Python is awesome!")
elif language == "java":
	print("Java is OK")
else:
	print(language + "is meh")


# We use for loops and while loops for repetition

# prints 0*0, 1*1, 2*2, ... 9*9
for i in range(0, 10)
	print(i * i)

# prints 0*0, 1*1, 2*2, ... 9*9 as well
i = 0
while i * i < 100:
	print(i * i)
	i = i + 1
'''



'''
CHALLENGE 1: Password 3.0

Let's say the user's password is "ilovepython". Ask them to enter their password until they get it right. However, if they get three wrong attempts, tell them that they've been locked out!
'''



'''
CHALLENGE 2: Inverse sum

Ask the user for a number S, and find the smallest n, so that 1+2+3+...+n is greater or equal to S.

Can you do it with a for loop? A while loop? With some math?
'''


