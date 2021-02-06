'''
INTRODUCTION TO
    ______  __________  ______  _   __
   / __ \ \/ /_  __/ / / / __ \/ | / /
  / /_/ /\  / / / / /_/ / / / /  |/ / 
 / ____/ / / / / / __  / /_/ / /|  /  
/_/     /_/ /_/ /_/ /_/\____/_/ |_/   
                                      
ACTIVITY 15: I Love Input! (Printing, variables, input)

Billiam loves asking the user unusual questions. He wants you to ask the user for their favorite sushi roll and print your own favorite sushi roll. Then, he wants you to ask the user for their age, and you should print your own age. Can you then print out the sum of both of your ages?
'''


fav_sushi = input("What is your favorite sushi role?")
print("My favorite sushi role is the Californian sushi role.")

age = input("What is your age?")
print("My age is 11 years old")

ans = 11 + int(age)
print("Together, our ages are " + str(ans))