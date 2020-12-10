'''
INTRODUCTION TO
    ______  __________  ______  _   __
   / __ \ \/ /_  __/ / / / __ \/ | / /
  / /_/ /\  / / / / /_/ / / / /  |/ / 
 / ____/ / / / / / __  / /_/ / /|  /  
/_/     /_/ /_/ /_/ /_/\____/_/ |_/   
                                      
READING INPUT

Let's say we want to find out what the user's name is. We can do that by using input()
It's quite easy once we see an example
'''


# Let's get some info about the user
print("What's your name?")

your_name = input() # type your name into the console

print("Your name is:")
print(your_name)


print("What's your age?")

your_age = input()

print("Your age is:")
print(your_age)

print("After your next birthday, you will be:")
# print(your_age + 1)

# Whoa!
# input() gets input as a string
# So, your_age is a string
# And you can't add 1 to a string, as we saw earlier!

# So, what do we do?
print("Your age, as a string:")
print(your_age)

# We can use int(your_age) to CONVERT your_age from a string into an integer
print("Your age, as an integer:")
print(int(your_age))

# Now it works!
print("After your next birthday, you will be:")
print(int(your_age) + 1)


first_name = "Bill"
last_name = "Wender"

# When we "add" two strings, we mash them together to create a new string
# this called "concatenating" if you want to use the fancy word
# "Bill" + "Wender" = "BillWender"
name = first_name + last_name

print("His name is:")
print(name)

# Oops! That doesn't look right.
# Let's add a space in the middle
name = first_name + " " + last_name
print("This should be better:")
print(name)



'''
ACTIVITY 4: What's wrong with this code?

Figure out what's wrong here!
'''

'''
ans = 5
# Print 2 + 2 = 5
print("2 + 2 = " + ans)
'''



'''
ACTIVITY 5: Converting between strings and integers

Ask for the user's age, then ask them what age they think they will finish school
Print the number of years of school left for them!
'''



