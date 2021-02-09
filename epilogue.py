'''
INTRODUCTION TO
    ______  __________  ______  _   __
   / __ \ \/ /_  __/ / / / __ \/ | / /
  / /_/ /\  / / / / /_/ / / / /  |/ / 
 / ____/ / / / / / __  / /_/ / /|  /  
/_/     /_/ /_/ /_/ /_/\____/_/ |_/   
                                      
EPILOGUE

The end. Remember to go through this at the end of the course!
'''


# Import some libraries
import os
import time


s = '''



		\033[1mCONGRATULATIONS!\x1b[0m


You've completed Intro to Python!
You've now unlocked a new superpower:

	\033[1mPROGRAMMING IN PYTHON!!!\x1b[0m


		\033[1mWHAT'S NEXT?\x1b[0m

Instal Python on your computer!
This gives you more flexibility for
writing and testing your Python code

It's really easy!
Go to https://www.python.org/downloads/
And click on download
Follow the instructions for your OS


		\033[1mGOOD SITES\x1b[0m

https://stackoverflow.com/
 - Great for looking up questions!

Basically any search engine
 - Also great for looking up questions!

https://pythondiscord.com/
 - The Python Discord!


	\033[1mSPECIAL THANKS TO\x1b[0m

	\033[1m\33[31m   Anthony Wang   \x1b[0m
	\033[1m\33[32m    Darren Teh    \x1b[0m
	\033[1m\33[33m   Samuel Chen    \x1b[0m
	\033[1m\33[34m   Richie Jiang   \x1b[0m
	\033[1m\33[35m     Andy Teh     \x1b[0m
	\033[1m\33[36m  Billiam Wender  \x1b[0m
	\033[1m\33[31m  Aiden Lambert   \x1b[0m
	\033[1m\33[32m     Jason Xu     \x1b[0m
	\033[1m\33[33m    Jason Ding    \x1b[0m
	\033[1m\33[34m  Bobert Render   \x1b[0m
	\033[1m\33[35m   Michael Cao    \x1b[0m
	\033[1m\33[36m     Leo Liu      \x1b[0m


		\033[1mTHANK YOU!\x1b[0m


INTRODUCTION TO
    ______  __________  ______  _   __
   / __ \ \/ /_  __/ / / / __ \/ | / /
  / /_/ /\  / / / / /_/ / / / /  |/ / 
 / ____/ / / / / / __  / /_/ / /|  /  
/_/     /_/ /_/ /_/ /_/\____/_/ |_/   
                                      

Copyleft 🄯 2021 Billiam Wender. All rights reversed.
'''


# Can you figure out what this does?
def credits():
	lines = s.split('\n')
	n = len(lines)
	i = 0
	while True:
		os.system('clear')
		for j in range(i, min(n-1, i+24)):
			print('    '+lines[j])
		time.sleep(1)
		i = i+1
		if i == n: i = 0


# roll the
credits()
# Thanks for watching!

