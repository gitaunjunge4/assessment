For example, given S = "We test coders. Give us a try?", there are three sentences: "We test coders", " Give us a try" and "". The first sentence contains three words: "We", "test" and "coders". The second sentence contains four words: "Give", "us", "a" and "try". The third sentence is empty.
Write a function:
def solution(S)
that, given a string S consisting of N characters, returns the maximum number of words in a sentence.
For example, given S = "We test coders. Give us a try?", the function should return 4, as explained above.
Given S = "Forget CVs..Save time . x x", the function should return 2, as there are four sentences: "Forget CVs" (2 words), "" (0 words), "Save time " (2 words) and " x x" (2 words).


define a function
split the text at (.?)
split the sentence at an empty space
intialize a var that holds max_words_no for a sentence
count the number of words in that sentence 
set max_words_no as the count 
return max_words_no
