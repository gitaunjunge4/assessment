#define a function 
#change the input to a list to make it mutable
# and also get the length
# init two pointers that will help you move from L-> R and R->L  L=0, R= Length -1
# iterate though the string from outer to inner as you move towards the centre checking if:
#  - both ends have ? replace with a for easiest palindrome
#  - L has letter and R has no letter; set value of R = to L
#  - R has letter and L has no letter; set value of L = to R
#  - L != R print statement 'NO'

# if the len statement is odd and the middle value is ? set 'a' as the letter

# return as string
def solution(text):
    S = list(text)
    len_of_str = len(S)
    # print(S)
    # print(len_of_str)
    left = 0 
    right = len_of_str - 1 

    while left < right:
        if S[left] == '?' and S[right] == '?':
            S[left] = S[right] = 'a'

        elif S[left] != '?' and S[right] == '?':
            S[right] = S[left]

        elif S[left] == '?' and S[right] != '?':
            S[left] = S[right]

        elif S[left] != S[right]:
            return print('NO!')

        left += 1
        right -= 1
        
    if len_of_str % 2 == 1 and S[len_of_str // 2]== '?':
       S[len_of_str // 2] = 'a' 
        
    return print("".join(S))


solution("hearmeoutt")
solution('ab??a')
