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
# input() will get INPUT from the user
# then we save that input in your_name

print("Your name is:")
print(your_name)


print("What's your age?")

your_age = input()

print("Your age is:")
print(your_age)


'''
Try it out yourself!
Let's do Activity 9!
'''


print("After your next birthday, you will be:")
print(your_age + 1)

# Whoa!
# input() gets input AS A STRING
# So, your_age is a STRING
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


'''
Let's do Activity 10!
'''


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
Let's do Activity 11, 12, 13, 14, and 15 now!
'''

