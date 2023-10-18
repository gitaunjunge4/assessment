# define a function 
# change the input to a list to make it mutable
# Initialize an alphabet string containing lowercase letters from 'a' to 'z'.
# Initialize an empty string to store the result
# init an empty string to hold prev letter
# Iterate through the characters in the list 'riddle' checking for a '?'.
# When ('?') is found, find a character that is different from the previous one before it and append it to the result string.
# brreak the loop when the fisrt valid letter is found
# if none is found: append the character to  result and also to the previous string
# If you reach the end of the letters, wrap around to 'a' again.
# Return the result string.
import random


# MY ANSWER
# def solution(riddle):
#     s = list(riddle)
#     # print(s)
#     letters = 'abcdefghijklmnopqrstuvwxyz'
#     # len_of_str = len(s)  
#     result = []
#     prev_letter = result[-1] if result else ''

#     # looping through each char in s chacking for ?
#     for char in s:
#         if char == '?':
#             # giving it a letter
#             for letter in letters:
#                 if letter != prev_letter:
#                     result.append(letter)
#                     prev_letter = letter  
#                     break
                    
#         else:
#             result.append(char)
#             prev_letter = char

#     return ("".join(result))

# print(solution("ab?ac?"))  



#CHAT ANSWER
# def a function
def solution(riddle):
    # initalize the alphabet
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    # change the input to list for mutability
    riddle_list = list(riddle)
    
    # loop through each character using index in riddle and comparing if the value at that index == ?
    for char in range(len(riddle)):
        print(char)
        if riddle[char] == '?':
            possible_chars = alphabet
            if char > 0 and riddle[char - 1] in possible_chars:
                possible_chars = possible_chars.replace(riddle[char - 1], '')
            if char < len(riddle) - 1 and riddle[char + 1] in possible_chars:
                possible_chars = possible_chars.replace(riddle[char + 1], '')
            
            if possible_chars:
                riddle_list[char] = random.choice(possible_chars)
            else:
                riddle_list[char] = random.choice(alphabet)
    
    return ''.join(riddle_list)

print(solution("ab?ac?")) 