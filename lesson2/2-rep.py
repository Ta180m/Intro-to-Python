'''
INTRODUCTION TO
    ______  __________  ______  _   __
   / __ \ \/ /_  __/ / / / __ \/ | / /
  / /_/ /\  / / / / /_/ / / / /  |/ / 
 / ____/ / / / / / __  / /_/ / /|  /  
/_/     /_/ /_/ /_/ /_/\____/_/ |_/   
                                      
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
# Imagine it is a repeat button. It will repeat the code a certain amount of times.
# A for loop in the range(1, x) will repeat the enclosed code x times

# It will repeat for every i in the range 1 (INCLUSIVE) to 11 (EXCLUSIVE)
# This means that it will repeat for every number from 1 to 10
# In general, a for loop on a range(x, y) will repeat for every
# number x, x + 1, ..., y - 2, y - 1
# Note that y is NOT included
'''


'''
ACTIVITY 4: Spammer

Print "python is awesome" 100 times!
'''



'''
ACTIVITY 5: Reversed!

Print the numbers from 1 to 10 in reverse order!

Hint: Instead of print(i), what else could we do?
'''



'''
ACTIVITY 6: Sum

Ask the user for a number n, and print the sum of the first n positive integers, basically, print the sum 1+2+3+...+n.
'''



'''
# However, sometimes we don't know how many times we want to repeat something
# Maybe we just want to repeat until a certain condition is satisfied
# We can use a WHILE loop


your_age = int(input())
while your_age < 16:
	print("You are only " + str(your_age) + ". You can't drive yet!")
	your_age = your_age + 1

print("You are " + str(your_age) + ". You can drive now!")

# We used a while loop here we don't know how many times we have to repeat
# The user could be 2 or 12 or 102

# What type is your_age?
# What type is your_age < 16?
# Why do we have to do str(your_age) when printing?
# Always remember types!
'''


'''
ACTIVITY 7: Exponential growth

A rabbit population starts out with 2 rabbits. Each year, the population size doubles. Find the number of years before the population reaches 1000 using a while loop!
'''



'''
ACTIVITY 8: Password 2.0

Let's say the user's password is "ilovepython". Ask them to enter their password until they get it right.
'''



'''
ACTIVITY 9: Infinite loop

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


