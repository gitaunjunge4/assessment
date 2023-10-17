There are two strings, A and B, each of length N. A fragment of string A corresponds with a fragment of string B if:
both fragments start at the same position;
letters from one fragment can be rearranged into the order of letters in the other fragment (note that the case and number of occurrences of the letter matters).
For example, given A = "dBacaAA" and B = "caBdaaA", fragment "Ba" starting at position 1 of string A corresponds with fragment "aB" starting at position 1 of string B. On the other hand, fragment "ca" at position 3 in A does not correspond to "ca" at position 0 in B as they start in different positions. Fragments "aAA" and "aaA" starting at position 4 of both strings do not correspond as the number of occurrences of letters 'a' and 'A' in the fragments differ.
Write a function:
int solution(char *A, char *B);
that, given strings A and B, each of length N, returns the number of corresponding fragments of A and B.
Examples:
1. Given A = "dBacaAA" and B = "caBdaaA", the function should return 5. The corresponding fragments are:
"dBaca" and "caBda" (starting at position 0)
"dBac" and "caBd" (starting at position 0)
"Ba" and "aB" (starting at position 1)
"a" and "a" (starting at position 4)
"A" and "A" (at position 6).
2. Given A = "zzzX" and B = "zzzX", the function should return 10. All fragments starting at the same positions in both strings correspond.
3. Given A = "abc" and B = "ABC", the function should return 0. Even though the fragments consist of the same letters, in string A they are lowercase and in string B they are uppercase.
4. Given A = "ZZXYOz" and B = "OOYXZZ", the function should return 2.