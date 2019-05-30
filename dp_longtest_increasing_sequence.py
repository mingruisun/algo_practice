# Bottom up approach

def lis(a):
    dp = [-1] * len(a)

    dp[0] = 1

    for i in range(1, len(a)):
        max_seq = -1
        found_smaller = False
        for j in range(i - 1, -1, -1):
            if a[i] > a[j] and dp[j] > max_seq:
                max_seq = dp[j]
                found_smaller = True
        if found_smaller:
            dp[i] = max_seq + 1
        else:
            dp[i] = 1

    # debugging print
    for i in range(len(a)):
        print("%d : %d" % (a[i], dp[i]))

    print(max(dp))

# top down approach

def lis_topDown(i, a, dp):

    # base case
    if i == 0:
        return 1

    dp[i] = lis_topDown(i-1, a, dp) + 1

# test driver
# for _ in range(int(input())):
#     size = int(input())
#     a = [int(x) for x in input().split()]
#     lis(a)

a = "86 177 115 193 135 186 92 49 21 162 27 90 59 163 126 140 26 172 136 11 168 167 29 182 130 62 123 67 135 129 2 22 58 69 167 193 56 11 42 29 173 21 119 184 137 198 124 115 170 13 126 91 180 156 73 62 170 196 81 105 125 84 127 136 105 46 129 113 57 124 95 182 145 14 167 34 164 43 150 87 8 76 178"

a = [int(x) for x in a.split()]

dp = [0] * len(a)

# lis(a)
lis_topDown(len(a), a, dp)

#  test case failed
# 83
# 86 177 115 193 135 186 92 49 21 162 27 90 59 163 126 140 26 172 136 11 168 167 29 182 130 62 123 67 135 129 2 22 58 69 167 193 56 11 42 29 173 21 119 184 137 198 124 115 170 13 126 91 180 156 73 62 170 196 81 105 125 84 127 136 105 46 129 113 57 124 95 182 145 14 167 34 164 43 150 87 8 76 178

# Its Correct output is:
# 15
#
# And Your Code's output is:
# 14

#  root cause: when there is a value inside the list that is smaller than any number before it, the max LIS at that point will not be updated, and left as -1 + 1 = 0, This is a bug.