Rick is a fan of logic-based games. However, he is bored of the classic ones, like Sudoku and Mastermind, since he has solved so many of them.
Recently he found a new game in which one is given a string with some question marks in it.


The objective is to replace all of the question marks with letters (one letter per question mark) in such a way that no letter appears next to another letter of the same kind.
Write a function:

def solution(riddle)
that, given a string riddle, returns a copy of the string with all of the question marks replaced by lowercase letters (a−z) in such a way that the same letters do not occur next to each other. The result can be any of the possible answers as long as it fulfils the above requirements.
Examples:
1. Given riddle = "ab?ac?", your function might return "abcaca". Some other possible results are "abzacd", "abfacf".
2. Given riddle = "rd?e?wg??", your function might return "rdveawgab".
3. Given riddle = "????????", your function might return "codility".

define a function 
the text should be split to a list
length of str =n
n+1
iterate through it and check for '?'; if it finds replace with a letter(n) that:
- n != n-1
- n != n+1 

if S[value] == '?':
 s[val] = 

join it back to string and print it 

define a function 
Initialize an empty list to keep track of the letters we have used.
Iterate through the characters in the input string, and for each character:
a. If the character is not a question mark, simply add it to the result string.
b. If the character is a question mark, find the next available letter (a to z) that doesn't match the letter before it. To do this, you can use a loop to check each letter from 'a' to 'z' and pick the first one that satisfies the condition. If there are no available letters, start from 'a' again. Add the chosen letter to the result string and append it to the list of used letters.
Return the final result string.
