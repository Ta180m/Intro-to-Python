'''
INTRODUCTION TO
    ______  __________  ______  _   __
   / __ \ \/ /_  __/ / / / __ \/ | / /
  / /_/ /\  / / / / /_/ / / / /  |/ / 
 / ____/ / / / / / __  / /_/ / /|  /  
/_/     /_/ /_/ /_/ /_/\____/_/ |_/   
                                      
ACTIVITY 14: Find the difference! (Functions)

Billiam and Bobert wrote the following codes. They look similar, but why do they produce different output?
'''


# Billiam's code
count = 0

def add_to_count():
	count = count + 1
	print("count is now = " + str(count))

for i in range(5):
	add_to_count()


# Bobert's code
count = 0

def add_to_count():
	global count
	count = count + 1
	print("count is now = " + str(count))

for i in range(5):
	add_to_count()

