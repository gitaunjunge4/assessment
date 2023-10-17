There is a company that sells large letters made out of wood and metal (similar to the ones spelling "HOLLYWOOD"). The company is going out of business, and the owners want to sell off their remaining stock. They have listed all the remaining letters in a catalogue in a string S (in no particular order), and have advertised their "Everything must go" offer online.
Attracted by the reduced prices, Alice has decided to order some letters from the company. She wants to build as many signs with the name of her new blog as possible and place them around the city. She hasn't decided on the name of her blog yet, and is considering K different possibilities. Right now she is wondering about the maximum number of signs she can build if she chooses one of the names from her list.
Knowing the list of possible names of Alice's blog L and the company catalogue state S, find the maximum number of copies of a name from L that Alice can build.
Write a function:
int solution(char *S, char *L[], int K);
that, given the string S and the list L consisting of K strings, returns the maximum number of copies of a string from L that can be built only using letters from S.
Examples:
1. Given S = "BILLOBILLOLLOBBI", L = ["BILL", "BOB"], the function should return 3. The sign "BILL" can be built three times using the letters from S and the sign "BOB" can be built only twice.
2. Given S = "CAT", L = ["ILOVEMYDOG", "CATS"], the function should return 0. None of the proposed names can be built using the letters from S.
3. Given S = "ABCDXYZ", L = ["ABCD", "XYZ"], the function should return 1. Both signs "ABCD" and "XYZ" can be built only once using the letters from S.
