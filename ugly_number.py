"""
# Ugly numbers are numbers whose only prime factors are 2, 3 or 5. The sequence 1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 15,shows the first 11 ugly numbers. By convention, 1 is included. Write a program to find Nth Ugly Number.
#
# Input:
# The first line of input contains an integer T denoting the number of test cases. T testcases follow. For each testcase there is one line of input that contains the number N.
#
# Output:
# Print the Nth Ugly Number.
#
# Constraints:
# 1 <= T <= 10^4
# 1 <= N <= 10^4
#
# Example:
# Input:
# 2
# 10
# 4
# Output:
# 12
# 4
#
# """


# problem analysis

"""
 1. subproblems (is this a suffix, prefix, substring problem?)
 
 I think this is a prefix problem
 
 2. guess(what's part of the solution?)
 
 trying to figure out how to get number[i]
 
 3. reoccurence
 
 4. run time
 
 5. original problem


"""


def uglyNum_BottomUp(n):
    dp = [-1] * n
    dp[0] = 1

    i2 = 0
    i3 = 0
    i5 = 0

    n2 = 2
    n3 = 3
    n5 = 5

    for i in range(1, n):
        dp[i] = min(n2, n3, n5)
        if dp[i] == n2:
            i2 += 1
            n2 = dp[i2] * 2
        if dp[i] == n3:
            i3 += 1
            n3 = dp[i3] * 3
        if dp[i] == n5:
            i5 += 1
            n5 = dp[i5] * 5
    print(dp)
    return dp[n-1]

print(uglyNum_BottomUp(11))

# def uglyNum_TopDown(n):

# driver
# for _ in range(int(input())):
#     temp = [int(x) for x in input().split()]
#     str1_size = temp[0]
#     str2_size = temp[1]
#     str1 = input()
#     str2 = input()