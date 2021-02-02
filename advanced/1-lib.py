'''
INTRODUCTION TO
    ______  __________  ______  _   __
   / __ \ \/ /_  __/ / / / __ \/ | / /
  / /_/ /\  / / / / /_/ / / / /  |/ / 
 / ____/ / / / / / __  / /_/ / /|  /  
/_/     /_/ /_/ /_/ /_/\____/_/ |_/   
                                      
USING LIBRARIES

Welcome to the first advanced lesson!
'''


# Python is a great language!
# But it doesn't have everything
# We can use LIBRARIES to extend what Python can do
# Libraries contain code that other people have written
# You can IMPORT them and build on top of other people's code!

# Let's look at a simple example
# Say we want to output colorful text
# First import a library
import termcolor

# Now we can use its functions!
termcolor.cprint('Hello, World!', 'green', 'on_red')

# The library termcolor contains the function cprint
# This function is similar to print but allows you to pass in two more arguments
# One controls the text color
# The other controls the background color

# You can find this library at https://pypi.org/project/termcolor
# PyPI is the Python Package Index
# It contains thousands of libraries packaged for you to use!
# It also has some useful information on how to use each library.

# Now let's work on Activites 1 and 2!


# termcolor was made by some random person
# And published to the PyPI
# However, our next example, random, is made by the same people behind Python
# random is part of the Python STANDARD LIBRARY
# You can find its information at https://docs.python.org/3/library/random.html

# We start off as usual
import random

print(random.randint(1, 6)) # Roll a dice

# Let's look at Activities 3 and 4!


# All of the standard libraries are at https://docs.python.org/3/library/
# You can find all other libraries at https://pypi.org/

# Let's do Activities 5 and 6 now!

