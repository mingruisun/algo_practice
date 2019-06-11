
'''

S(n+1, k) = k*S(n, k) + S(n, k-1)
'''
def bell_numbers_naive_helper(n, k):
    if n < k or k <= 0 or n <= 0:
        return 0
    if n == k or n == 1 or k == 1:
        return 1

    return k * bell_numbers_naive_helper(n - 1, k) + bell_numbers_naive_helper(n - 1, k - 1)

def bell_numbers_naive(n):

    sum = 0
    for i in range(1, n + 1):
        sum += bell_numbers_naive_helper(n, i)
    return sum

print(bell_numbers_naive(5))

def bell_numbers_topdown_helper(n, k, dp):
    if n < k or k <= 0 or n <= 0:
        dp[n][k] = 0
        return dp[n][k]
    if n == k or n == 1 or k == 1:
        dp[n][k] = 1
        return dp[n][k]

    if dp[n][k] != -1:
        return dp[n][k]
    else:
        dp[n][k] = k * bell_numbers_topdown_helper(n - 1, k, dp) + bell_numbers_topdown_helper(n - 1, k - 1, dp)
        return dp[n][k]

def bell_numbers_topdown(n):
    dp = [[-1 for i in range(n + 1)] for j in range(n + 1)]


    sum = 0
    for i in range(1, n + 1):
        sum += bell_numbers_topdown_helper(n, i, dp)

    for i in dp:
        print(i)
    return sum

print(bell_numbers_topdown(5))