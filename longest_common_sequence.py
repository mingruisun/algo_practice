

# driver
# for _ in range(int(input())):
#     temp = [int(x) for x in input().split()]
#     str1_size = temp[0]
#     str2_size = temp[1]
#     str1 = input()
#     str2 = input()
#

def printDp(dp):

    for i in range(len(dp)):
        print(dp[i])

def lcs(str1, str2, dp):

    if str1[0] == str2[0]:
        dp[0][0] = 1
    for i in range(1, len(str1)):
        if str2[0] == str1[i]:
            dp[0][i] = 1
        else:
            dp[0][i] = dp[0][i-1]

    for i in range(1, len(str2)):
        if str1[0] == str2[i]:
            dp[i][0] = 1
        else:
            dp[i][0] = dp[i-1][0]

    # printDp(dp)
    for i in range(1, len(str2)):
        for k in range(1, len(str1)): # going horizontally first
            if str1[k] == str2[i]:
                dp[i][k] = dp[i-1][k-1] + 1

            else:
                dp[i][k] = max(dp[i - 1][k], dp[i][k - 1])

    # the solution will be the bottom right most cell

    printDp(dp)
    print(dp[len(str2)-1][len(str1)-1])
#
# str1_size = 83
# str2_size = 86
# str1 = "LRBBMQBHCDARZOWKKYHIDDQSCDXRJMOWFRXSJYBLDBEFSARCBYNECDYGGXXPKLORELLNMPAPQFWKHOPKMCO"
# str2 = "QHNWNKUEWHSQMGBBUQCLJJIVSWMDKQTBXIXMVTRRBLJPTNSNFWZQFJMAFADRRWSOFSBCNUVQHFFBSAQXWPQCAC"

# str1_size = 6
# str2_size = 7
# str1 = "AGGTAB"
# str2 = "GXTXAYB"

# a special case that fails
str1_size = 6
str2_size = 3
str1 = "ABCABC"
str2 = "ABB"


# str1 will be used as x-axis in the dp state space
# str2 will be used as y-axis in the dp state space

dp = [[0 for i in range(str1_size)] for j in range(str2_size)]



lcs(str1, str2, dp)



# failed test case

'''
Input:
83 86
LRBBMQBHCDARZOWKKYHIDDQSCDXRJMOWFRXSJYBLDBEFSARCBYNECDYGGXXPKLORELLNMPAPQFWKHOPKMCO
QHNWNKUEWHSQMGBBUQCLJJIVSWMDKQTBXIXMVTRRBLJPTNSNFWZQFJMAFADRRWSOFSBCNUVQHFFBSAQXWPQCAC

Its Correct output is:
25

And Your Code's output is:
36

'''