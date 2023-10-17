# PSEUDOCODE
# define a function that takes in S as a string in as its args
# create var 
# 

import re
def solution(S):
    # define a dict to map words to thier corresponding values
    word_to_value = {"one": 1, "two": 2}

    # splitting the input by operators ("+" and "-") and store the elements in a list
    # square brackets [] create a character class that matches any one of the characters inside it
    # parentheses ( ) are used to capture the matched character as a separate element in the output list.
    elements = re.split(r'([+-])', S)
    # print(elements)

    # initialize the result to the value of the first word in the list
    result = word_to_value[elements[0]]

    # iterate through the elements in the list and peform the calculations
    for i in range (1, len(elements), 2): # start at index 1 and step by 2 to get the operates and do this for the len of elements
        operator = elements[i]
        word=elements[i+1]

        if operator == "+":
            result += word_to_value[word]
        elif operator == "-":
            result -= word_to_value[word]

        print(result)
        return result


solution(("two-two-one-two"))
solution(("two"))