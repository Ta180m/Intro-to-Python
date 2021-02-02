'''
INTRODUCTION TO
    ______  __________  ______  _   __
   / __ \ \/ /_  __/ / / / __ \/ | / /
  / /_/ /\  / / / / /_/ / / / /  |/ / 
 / ____/ / / / / / __  / /_/ / /|  /  
/_/     /_/ /_/ /_/ /_/\____/_/ |_/   
                                      
EPILOGUE
'''


# Import some libraries
import os
import time


s = '''
Congratulations!
You've completed Intro to Python!
You've now unlocked a new superpower: programming with Python!


What's next?

Instal Python on your computer!
This gives you more flexibility for writing and testing Python code

It's really easy!
Go to https://www.python.org/downloads/
And click on download
Follow the instructions for your OS


Good sites:

https://stackoverflow.com/
 - Great for looking up questions!

Basically any search engine
 - Also great for looking up questions!

More ideas?


Special Thanks To:
 - Anthony Wang
 - Darren Teh
 - Samuel Chen
 - Richie Jian
 - Andy Teh
 - Aiden Lambert
 - Jason Xu
 - Michael Cao
 - Jason Ding
'''


# Can you figure out what this does?
def credits():
	lines = s.split('\n')
	n = len(lines)
	i = 0
	while True:
		os.system('clear')
		for j in range(i, min(n-1, i+16)):
			print(lines[j])
		time.sleep(0.5)
		i = i+1
		if i == n: i = 0


credits()

