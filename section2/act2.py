'''
INTRODUCTION TO
    ______  __________  ______  _   __
   / __ \ \/ /_  __/ / / / __ \/ | / /
  / /_/ /\  / / / / /_/ / / / /  |/ / 
 / ____/ / / / / / __  / /_/ / /|  /  
/_/     /_/ /_/ /_/ /_/\____/_/ |_/   
                                      
ACTIVITY 2: Your Age 2.0 (Conditionals)

ASK the user for their age, then tell them what stage of life (baby, kid, teenager, adult, etc) they are in right now.

Hint: Use input() and print()
'''

age = 15

#our age is more than 3
if (age <= 3):  
  print("Baby")
if (4 < age < 12):  #(4 <= age <= 12)
  print("Child")
if (13 < age < 17): #(13 <= age <= 17)
  print("Teen")
else: 
  print("Adult")
