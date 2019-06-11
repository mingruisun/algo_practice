def factorial(n, dp):
    if n <= 1:
        return 1
    if dp[n] == -1:
        dp[n] = n * factorial(n - 1, dp)
    return dp[n]

def binomial_coeff_naive(n, k):
    dp = [-1] * (n + 1)

    return factorial(n, dp) / (factorial(k, dp) * factorial(n - k, dp))

print(binomial_coeff_naive(4, 2))

