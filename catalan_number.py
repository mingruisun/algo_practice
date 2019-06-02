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

def catalan_number_naive(n):
    if n <= 1:
        return 1
    cat = 0
    for i in range(0, n):
        cat += catalan_number_naive(i) * catalan_number_naive(n - 1 - i)
    return cat

print(catalan_number_naive(10))