There is a string S made of words "one" and "two" separated by single "+" and "-" signs. The string represents a valid sequence of additions and subtractions of the digits 1 and 2.
Calculate the result of the expression represented by S.
Write a function:
def solution(S)
that, given a string S, returns the result of the mathematical expression it represents.
Examples:
1. Given S = "one+two-one-one+two+one", the string represents the expression 1 + 2 − 1 − 1 +  + 1. Its result is equal to 4. The function should return 4.
2. Given S = "two-two-one-two", the function should return −3.
3. Given S = "two", the function should return 2.
