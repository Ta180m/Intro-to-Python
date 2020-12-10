'''
INTRODUCTION TO
    ______  __________  ______  _   __
   / __ \ \/ /_  __/ / / / __ \/ | / /
  / /_/ /\  / / / / /_/ / / / /  |/ / 
 / ____/ / / / / / __  / /_/ / /|  /  
/_/     /_/ /_/ /_/ /_/\____/_/ |_/   
                                      
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
	print(language + " is meh")


# We use for loops and while loops for repetition

# prints 0*0, 1*1, 2*2, ... 9*9
for i in range(0, 10)
	print(i * i)

# prints 0*0, 1*1, 2*2, ... 9*9 as well
i = 0
while i * i < 100:
	print(i * i)
	i = i + 1

# We typically use for loops when we know the number of repetitions in advance
# And while loops when we aren't sure how many times we need to repeat
'''



'''
CHALLENGE 1: Password 3.0

Let's say the user's password is "ilovepython". Ask them to enter their password until they get it right. However, if they get three wrong attempts, tell them that they've been locked out!
'''



'''
CHALLENGE 2: Inverse sum

Ask the user for a number S, and find the smallest n, so that 1+2+3+...+n is greater or equal to S.

Can you do it with a while loop? A for loop? With some math?
'''


