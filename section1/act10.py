'''
INTRODUCTION TO
    ______  __________  ______  _   __
   / __ \ \/ /_  __/ / / / __ \/ | / /
  / /_/ /\  / / / / /_/ / / / /  |/ / 
 / ____/ / / / / / __  / /_/ / /|  /  
/_/     /_/ /_/ /_/ /_/\____/_/ |_/   
                                      
ACTIVITY 10: Triple Sum (Printing, variables, input)

Billiam can find the sum of two numbers, but he can't do the quick maths needed to find the sum of three numbers. Ask the user for three integers, one at a time, then print their sum.
'''

numone = input("What is your first number?")
numtwo = input("What is your second number?")
numthree = input("What is your third number?")

sum = int(numone) + int(numtwo) + int(numthree)
print(sum)