'''
Given a number n, print n-th Fibonacci Number.
Examples:

Input  : n = 2
Output : 1

Input  : n = 9
Output : 34
'''

def fibonacci_naive(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci_naive(n - 1) + fibonacci_naive(n - 2)

# print(fibonacci_naive(9))

# DP top down

def fib_helper(n, dp):
    if n == 0:
        return 0
    if n == 1:
        return 1

    if dp[n] != -1:
        return dp[n]
    else:
        dp[n] = fib_helper(n - 1, dp) + fib_helper(n - 2, dp)
        return dp[n]

def fibonacci_topDown(n):
    dp = [-1] * (n + 1)
    dp[0] = 0
    dp[1] = 1

    fib_helper(n, dp)
    return dp[-1]

print(fibonacci_topDown(9))

# DP bottom up

def fibonacci_bottomUp(n):
    dp = [-1] * (n+1)
    dp[0] = 0
    dp[1] = 1

    for i in range(2, n+1):
        dp[i] = dp[i-1] + dp[i-2]
    print(dp)
    return dp[-1]

# print(fibonacci_bottomUp(9))
