You are given a string S consisting of N characters.
The string is a valid phone number if it consists of three segments of digits (each three digits long) separated by single dashes.
Write a function:
int solution(char *S);
that, given a string S of length N, returns 1 if the string S represents a valid phone number and 0 if it doesn't.
Examples:
1. Given string S = "123-123-123", the function should return 1.
2. Given string S = "123 123 123", the function should return 0, because the segments are separated by spaces instead of dashes.
3. Given string S = "123-123-1234", the function should return 0, because there are too many digits in the last segment.
4. Given string S = "001-501-511", the function should return 1.
5. Given string S = "123-abc-123", the function should return 0, because S contains letters.
