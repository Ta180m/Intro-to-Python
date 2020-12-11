'''
INTRODUCTION TO
    ______  __________  ______  _   __
   / __ \ \/ /_  __/ / / / __ \/ | / /
  / /_/ /\  / / / / /_/ / / / /  |/ / 
 / ____/ / / / / / __  / /_/ / /|  /  
/_/     /_/ /_/ /_/ /_/\____/_/ |_/   
                                      
FOR LOOPS

The world is full of repetition: you sleep and wake up every day, scientists repeat experiments many times to confirm their results, and history repeats itself (Read https://en.wikipedia.org/wiki/Historic_recurrence#Similarities if you don't believe me)

Computers were originally invented to automate computation, so they are also full of repetition. Let's see how we can use repetition in programs.
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
Let's try Activities 7 and 8!
'''


# Let's say we want to compute 1 * 2 * 3 * 4 * ... * 10
# Again, we can use a for loop to save time!
product = 1
for i in range(2, 11): # i loops from 2, 3, 4, ... 10
    # Each time, multiply the existing product by the next i
	product = product * i

print(product)


'''
Let's look at Activities 9 and 10 now!
'''

