'''
INTRODUCTION TO
    ______  __________  ______  _   __
   / __ \ \/ /_  __/ / / / __ \/ | / /
  / /_/ /\  / / / / /_/ / / / /  |/ / 
 / ____/ / / / / / __  / /_/ / /|  /  
/_/     /_/ /_/ /_/ /_/\____/_/ |_/   
                                      
ACTIVITY 15: I Love Functions! (Functions)

Billiam really loves functions! He wants to write a function that takes in his list and Bobert's list, then returns a NEW longer list with Bobert's items added to the end of Billiam's list. Make sure you don't modify the original lists that they pass into the function!
'''


def merge_lists(Billiam_list, Bobert_list):
    # Create a NEW longer list here



Billiam_list = [2, 3.14, True, [1, 4]]
Bobert_list = ["Hi", "my", "name", "is", "Bobert"]

print("Billiam's list: " + Billiam_list)
print("Bobert's list: " + Bobert_list)

new_merged_list = merge_lists(Billiam_list, Bobert_list)

print("New merged list: " + new_merged_list)
print("Billiam's list: " + Billiam_list)
print("Bobert's list: " + Bobert_list)


