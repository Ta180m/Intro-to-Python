'''
INTRODUCTION TO
    ______  __________  ______  _   __
   / __ \ \/ /_  __/ / / / __ \/ | / /
  / /_/ /\  / / / / /_/ / / / /  |/ / 
 / ____/ / / / / / __  / /_/ / /|  /  
/_/     /_/ /_/ /_/ /_/\____/_/ |_/   
                                      
ACTIVITY 14: Stuck in School (Printing, variables, input)

Ask for the user's age, then ask them what age they think they will finish school. Print the number of years of school left for them!
'''

age = input("What is your age?")
age_finish = input("What is your age when you finish school?")

difference = int(age_finish) - int(age)
print(difference)