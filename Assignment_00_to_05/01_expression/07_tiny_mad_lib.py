# Mad Libs is a word game where players are prompted for one word at a time, and the words are
# eventually filled into the blanks of a word template to make an entertaining story! We've 
# provided you with the beginning of a sentence (the SENTENCE_START constant) which will end in
#  a user-inputted adjective, noun, and then verb.


# Taking  inputs
adjective = input("Please type an adjective and press enter: ")
noun = input("Please type a noun and press enter: ")
verb = input("Please type a verb and press enter: ")

# Constructing the final sentence
SENTENCE_START = "Code in Place is fun."
final_sentence = f"{SENTENCE_START} I learned to program and used Python to make my {adjective} {noun} {verb}!"

# Displaying the fun result
print(final_sentence)
