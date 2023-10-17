import re

# def a function
def solution(text):
    # split the text into sentences at the following (. ! ?) characters
    sentences = re.split('[.!?]', text)

    # set the initial values of max count and max sentence 
    max_sentence = ""
    max_word_count = 0

    for sentence in sentences:
        # splitting the sentence into words at empty spaces
        words = sentence.split()
        # print(words)

        # counts the number of valid words in the sentence
        # isalpha() checks if a charcater is in the alphabet and returns true
        valid_word_count = sum(1 for word in words if any(char.isalpha() for char in word))
        # print (valid_word_count)

        # checks if the word count > than current word count 
        # True -> sets the word count as the value of the max word count
        # and also the sentence as that gives the max word count as the new max sentence
        if valid_word_count > max_word_count:
            max_word_count = valid_word_count
            max_sentence = sentence

    return print(max_sentence.strip())

text = "A sentence can be divided into words by splitting it at spaces. A sentence without words is valid, but a valid word must contain at least one letter."
solution(text)