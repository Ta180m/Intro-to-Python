'''
INTRODUCTION TO
    ______  __________  ______  _   __
   / __ \ \/ /_  __/ / / / __ \/ | / /
  / /_/ /\  / / / / /_/ / / / /  |/ / 
 / ____/ / / / / / __  / /_/ / /|  /  
/_/     /_/ /_/ /_/ /_/\____/_/ |_/   
                                      
DICTIONARIES

TODO
'''

# list of key value pairs
# keys are always strings
# keys must be unique

my_dict = {
  "name": "Bob",
  "year": 2000,
}
print(my_dict)
print("Hello", my_dict["name"])
my_dict["year"] = 1234
my_dict["age"] = 787
print(my_dict)

# Make sure you use activites 7-10
#SETS

# sets are lists without duplicate items
my_set = {123,"abc",123,True}
print(my_set)

my_list = [5,1,3,3,5,5,5]
unique_items = set(my_list)
print(unique_items)

# sets cannot contain other lists or sets