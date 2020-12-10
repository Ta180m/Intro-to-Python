'''
INTRODUCTION TO
    ______  __________  ______  _   __
   / __ \ \/ /_  __/ / / / __ \/ | / /
  / /_/ /\  / / / / /_/ / / / /  |/ / 
 / ____/ / / / / / __  / /_/ / /|  /  
/_/     /_/ /_/ /_/ /_/\____/_/ |_/   
                                      
ACTIVITY 11: Infinite loop (Conditionals, while loops)

Bob wrote the following code for Activity 8. What happens when the following code runs? How can we fix it?
'''

num_rabbits = 2
years = 0
while num_rabbits > 0:
	num_rabbits = 2 * num_rabbits
	years = years + 1
print(years)

