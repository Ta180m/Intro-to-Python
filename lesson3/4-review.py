'''
INTRODUCTION TO
    ______  __________  ______  _   __
   / __ \ \/ /_  __/ / / / __ \/ | / /
  / /_/ /\  / / / / /_/ / / / /  |/ / 
 / ____/ / / / / / __  / /_/ / /|  /  
/_/     /_/ /_/ /_/ /_/\____/_/ |_/   
                                      
REVIEW

This lesson, we looked over types and learned lists and functions.
'''

# We first went over some common types, such as integers, strings, booleans, and floats.
# We recalled that it is extremely important to remember what type your variables are.
# You can also use type(your_variable_name_here) to print the type if you are not sure

weird_var = 0.0
print(type(weird_var))


# We looked at another very useful data type today: lists.

# Lists are extremely versatile and can even contain other lists as items.
# Paired with for loops, they are even more powerful.

# Analyze the words in a sentence typed in by the user:
print("Type a sentence!")
sentence = input()
print("Your sentence was: " + sentence)

# break up sentence into a list of words
words = sentence.split()

# Now iterate through each word in the list of words
for word in words:
    # Use len( ) to get the number of letters in a word
    # len( ) returns us an integer, so we need to convert it to a string in order to mash it with the other strings
    print(word + " has " + str(len(word)) + " letters")

print() # print a newline


# Note that in Python, the first item on the list has INDEX 0, the second has index 1, and so on. The last item has index len(your_list) - 1, or index -1 as shorthand.


# We also looked at functions, which allow us to break up complicated tasks into smaller ones.

# What if we need to analyze a lot of sentences?
def analyze_sentence(sentence): # make sure you have the : colon here!
    print("Your sentence was: " + sentence)

    # break up sentence into a list of words
    words = sentence.split()

    sum_of_word_lens = 0
    for word in words:
        # Use len( ) to get the number of letters in a word
        # len( ) returns us an integer, so we need to convert it to a string in order to mash it with the other strings
        print(word + " has " + str(len(word)) + " letters")

        sum_of_word_lens = len(word) + sum_of_word_lens
    
    print() # print a newline

    # Find the average
    # len(words) gives us length of the list of words; basically the number of words in the sentence
    average_word_length = sum_of_word_lens / len(words) 
    
    # Return the total sum of all the word len
    return average_word_length


# Now we can use our function!
analyze_sentence("Hello my name is Bob")
analyze_sentence("Bob is better than Billiam")
analyze_sentence("I really really really love Python")


'''
Activites 13, 14, and 15 are review.

If you think you know the content well, try Challenges 1 and 2!
'''

