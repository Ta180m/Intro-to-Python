'''
INTRODUCTION TO
    ______  __________  ______  _   __
   / __ \ \/ /_  __/ / / / __ \/ | / /
  / /_/ /\  / / / / /_/ / / / /  |/ / 
 / ____/ / / / / / __  / /_/ / /|  /  
/_/     /_/ /_/ /_/ /_/\____/_/ |_/   
                                      
WHILE LOOPS

Sometimes we don't know how many times we want to repeat something
Maybe we just want to repeat until a certain condition is satisfied
We can use a WHILE loop
'''


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


# Here's another example when we don't know how many times to repeat
# Ask the user for their current amount of money 
money = input()
# Let's say their income each day is 5 dollars
income = 5
# Let's find out how long it takes them to save up 100 dollars
days = 0
while money < 100
    if days > 10:
        # We don't want to wait so long!
        # We can stop immediately using break
        break
    
    # You don't have enough, so you need another day
    days = days + 1
    # Add your daily income to you current money
    money = money + income

if money >= 100:
    print("You have to wait " + str(days) + " days to save up 100 dollars")
else:
    print("You have to wait more than 10 days. I can't wait that long!")


'''
Now let's look at Activities 8, 9, and 10!
'''

