'''
INTRODUCTION TO
    ______  __________  ______  _   __
   / __ \ \/ /_  __/ / / / __ \/ | / /
  / /_/ /\  / / / / /_/ / / / /  |/ / 
 / ____/ / / / / / __  / /_/ / /|  /  
/_/     /_/ /_/ /_/ /_/\____/_/ |_/   
                                      
REVIEW

Let's go over what we learned in this lesson!
'''


# Variables have a NAME, a VALUE, and a TYPE
# The type of a variable is VERY IMPORTANT
# Always keep track of what the type of your variables


# You can't mix and match different types when doing addition

# Addition will actually add two integer
sum = 2 + 2 # OK

# Addition will mash together (concatenate) two strings
full_name = "Bill" + " " + "Wender" # OK

# Addition doesn't work when the types are different!
bad = "2" + 2 # ERROR, "2" is a string while 2 is an integer


# We can get input using input()
print("What's your grade?")

your_grade = input() # saves input to the variable your_grade
# Now your_grade contains whatever the user typed in

# Mash together "Your grade is " and the variable your_grade
print("Your grade is " + your_grade)

# input() always gives us a string
# So your_grade is a string
# We have to CONVERT your_grade to an integer before we can add 1
# Then we need to convert it back into a string to mash it with "Next year ... "
print("Next year you will be in grade " + str(int(your_grade) + 1))


