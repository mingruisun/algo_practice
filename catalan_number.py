"""
Given a number N. The task is to find the nth catalan number.
The first few Catalan numbers for n = 0, 1, 2, 3,  are 1, 1, 2, 5, 14, 42, 132, 429, 1430, 4862

Input:
First line of input contains a single integer T which denotes the number of test cases. First line of each test case contains a single integer N.

Output:
For each test case, in a new line print the catalan number at position N.
Note: Positions start from 0 as shown above.

Constraints:
1 <= T <= 100
1 <= N <= 100

Example:
Input:
3
5
4
10

Output:
42
14
16796
"""

import utils

logging_run_time = utils.program_run_time()

def catalan_number_naive(n):
    if n <= 1:
        return 1
    cat = 0
    for i in range(0, n):
        cat += catalan_number_naive(i) * catalan_number_naive(n - 1 - i)
    return cat


def catalan_topdown_helper(n, dp):
    if n <= 1:
        return 1

    if dp[n] != -1:
        return dp[n]

    cat = 0
    for i in range(0, n):
        cat += catalan_number_naive(i) * catalan_number_naive(n - 1 - i)
        dp[n] = cat
    return cat

def catalan_number_topdown(n):
    dp = [-1] * (n + 1)
    dp[1] = 1
    dp[0] = 1

    catalan_topdown_helper(n, dp)
    return dp[-1]

def catalan_number_bottomUp(n):
    dp = [-1] * (n + 1)
    dp[0] = 1
    dp[1] = 1

    for i in range(2, n+1):
        cat = 0
        for j in range(0, i):
            cat += dp[j] * dp[i - j - 1]
        dp[i] = cat
    return dp[-1]

############# testing ##################
logging_run_time.reset_start_time()
print(catalan_number_naive(14))
logging_run_time.report_total_runtime("Naive method")

logging_run_time.reset_start_time()
print(catalan_number_topdown(14))
logging_run_time.report_total_runtime("top down method")

logging_run_time.reset_start_time()
print(catalan_number_bottomUp(14))
logging_run_time.report_total_runtime("bottom up method")


#### Note ####
'''
14th catalan number run time result

2674440
Total run time of Naive method is 0.5287871
2674440
Total run time of top down method is 0.4937291
2674440
Total run time of bottom up method is 2.5e-05
'''