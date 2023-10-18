# define a function
# split the text at (.?)
# loop through each sentence and split at an empty space and set word_count as lenght of the list
# intialize a var that holds max_words_no for a sentence
# count the number of words in that sentence 
# set max_words_no as the count 
# return max_words_no

import re 

def solution(text):
    sentences = re.split('[.?]', text)
    # print(sentences)
    max_words = 0
    # print(len(sentence))
    for sentence in sentences:
        words_in_sentence = sentence.split()
        word_count = len(words_in_sentence)
        print(words_in_sentence)
        if word_count > max_words:
            max_words = word_count
        
    return print(max_words)

text = "We test coders. Give us a try?"
solution(text)