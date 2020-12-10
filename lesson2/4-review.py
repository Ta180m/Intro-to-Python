'''
INTRODUCTION TO
    ______  __________  ______  _   __
   / __ \ \/ /_  __/ / / / __ \/ | / /
  / /_/ /\  / / / / /_/ / / / /  |/ / 
 / ____/ / / / / / __  / /_/ / /|  /  
/_/     /_/ /_/ /_/ /_/\____/_/ |_/   
                                      
REVIEW
'''


# This lesson we learned two important building blocks for making more sophisticated programs
# CONDITIONALS: if / elif / else
# REPETITION: for loops / while loops


# We use if / elif (else if) / else so the computer can make decisions

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










