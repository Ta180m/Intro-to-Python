'''
INTRODUCTION TO
    ______  __________  ______  _   __
   / __ \ \/ /_  __/ / / / __ \/ | / /
  / /_/ /\  / / / / /_/ / / / /  |/ / 
 / ____/ / / / / / __  / /_/ / /|  /  
/_/     /_/ /_/ /_/ /_/\____/_/ |_/   
                                      
ACTIVITY 11: Find the difference!

They look similar, but why do they produce different output?
'''

# 1)
count = 0

def addToCount():
	count = count + 1
	print("count is now = " + count)

for i in range(5):
	addToCount()

# 2)
count = 0

def addToCount():
	global count
	count = count + 1
	print("count is now = " + count)

for i in range(5):
	addToCount()

