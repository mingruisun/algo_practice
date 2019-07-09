import utils

logging_run_time = utils.program_run_time()

def knap_sack_naive(item, total_weight, weight_list, value_list):

    if item == -1 or total_weight == 0:
        return 0

    if weight_list[item] > total_weight:
        return knap_sack_naive(item - 1, total_weight, weight_list, value_list)

    return max(value[item] + knap_sack_naive(item - 1, total_weight - weight_list[item], weight_list, value_list), knap_sack_naive(item - 1, total_weight, weight_list, value_list))

def knap_sack_topDown_dp(item, total_weight, weight_list, value_list, dp):

    if item == -1 or total_weight == 0:
        return 0

    if weight_list[item] > total_weight:
        return knap_sack_topDown_dp(item - 1, total_weight, weight_list, value_list, dp)

    if dp[item][total_weight] == -1:
        dp[item][total_weight] = max(value[item] + knap_sack_topDown_dp(item - 1, total_weight - weight_list[item], weight_list, value_list, dp), knap_sack_topDown_dp(item - 1, total_weight, weight_list, value_list, dp))
    return dp[item][total_weight]


def knap_sack_bottomUp_dp(item, total_weight, weight_list, value_list, dp):
    for w in range(0, total_weight + 1):
        if weight[0] > w:
            dp[0][w] = 0
        else:
            dp[0][w] = value_list[0]

    for i in range(0, item + 1):
        dp[i][0] = 0
    for i in range(1, item + 1):
        for w in range(1, total_weight + 1):
            if weight_list[i] > w:
                dp[i][w] = dp[i - 1][w]
            else:
                dp[i][w] = max(dp[i - 1][w], value_list[i] + dp[i - 1][w - weight_list[i]])

    return dp[item][total_weight]

# value = [55, 61, 51, 75, 17, 22, 4, 13, 39, 28, 77, 49, 46, 91, 14, 67, 88, 62, 25, 37, 69, 38, 59, 62, 48, 88, 100, 53]
# weight = [96, 16, 34, 53, 88, 6, 50, 26, 76, 10, 8, 4, 37, 18, 73, 54, 30, 31, 97, 2, 28, 24, 2, 30, 79, 77, 33, 86]
# total_weight = 83
# item = len(value) - 1

# value = [60, 100, 120]
# weight = [10, 20, 30]
# total_weight = 50
# item = len(value) - 1

value = [51, 94, 66, 55, 81, 99, 79, 12, 14, 32, 36, 88, 65, 79, 62, 37, 47, 13, 93, 77, 100, 26, 44, 66, 73, 71, 74, 27, 6, 43, 16, 50, 7, 65, 3, 58, 7, 90, 99, 60, 84, 54, 68, 45, 28, 5, 43, 77, 47, 68, 9, 83, 66, 20, 84, 67, 4, 70, 90, 80, 11, 72, 54, 63, 9, 91, 43, 44, 36, 89, 60, 92, 70, 13, 66, 43, 45, 20, 32, 22, 61, 94, 25, 79, 27]
weight = [6, 89, 12, 23, 22, 72, 2, 25, 47, 40, 51, 93, 15, 49, 85, 43, 88, 75, 96, 72, 72, 26, 90, 46, 17, 69, 74, 73, 7, 25, 35, 27, 7, 19, 77, 53, 11, 21, 20, 32, 39, 45, 24, 19, 54, 94, 85, 9, 38, 19, 40, 37, 40, 53, 62, 32, 47, 20, 19, 51, 90, 5, 89, 50, 68, 63, 59, 8, 64, 16, 24, 51, 13, 37, 76, 63, 68, 32, 12, 18, 12, 60, 45, 39, 64]
item = len(value) - 1
total_weight = 50
dp = [ [-1 for x in range(total_weight + 1)] for x in range(item + 1)]


logging_run_time.reset_start_time()
print(knap_sack_naive(item, total_weight, weight, value))
logging_run_time.report_total_runtime("Naive method")

logging_run_time.reset_start_time()
print(knap_sack_topDown_dp(item, total_weight, weight, value, dp))
logging_run_time.report_total_runtime("top down method")


logging_run_time.reset_start_time()
print(knap_sack_bottomUp_dp(item, total_weight, weight, value, dp))
logging_run_time.report_total_runtime("bottom up method")

""" driver code
for t in range(int(input())):
    item = int(input())
    total_weight = int(input())
    value = [int(x) for x in input().split()]
    weight = [int(x) for x in input().split()]
    dp = [ [-1 for x in range(total_weight + 1)] for x in range(item + 1)]
    print(knap_sack(item, total_weight, weight, value, dp))
"""


""" expected output
For Input:
2
28
83
55 61 51 75 17 22 4 13 39 28 77 49 46 91 14 67 88 62 25 37 69 38 59 62 48 88 100 53 
[55, 61, 51, 75, 17, 22, 4, 13, 39, 28, 77, 49, 46, 91, 14, 67, 88, 62, 25, 37, 69, 38, 59, 62, 48, 88, 100, 53]
96 16 34 53 88 6 50 26 76 10 8 4 37 18 73 54 30 31 97 2 28 24 2 30 79 77 33 86 
[96, 16, 34, 53, 88, 6, 50, 26, 76, 10, 8, 4, 37, 18, 73, 54, 30, 31, 97, 2, 28, 24, 2, 30, 79, 77, 33, 86]

16
98
20 16 45 73 99 87 38 53 99 99 38 65 22 17 17 51 
31 21 78 53 18 66 61 4 11 65 16 99 87 91 44 23
Output of Online Judge is:
474
356


85
50
51 94 66 55 81 99 79 12 14 32 36 88 65 79 62 37 47 13 93 77 100 26 44 66 73 71 74 27 6 43 16 50 7 65 3 58 7 90 99 60 84 54 68 45 28 5 43 77 47 68 9 83 66 20 84 67 4 70 90 80 11 72 54 63 9 91 43 44 36 89 60 92 70 13 66 43 45 20 32 22 61 94 25 79 27
[51, 94, 66, 55, 81, 99, 79, 12, 14, 32, 36, 88, 65, 79, 62, 37, 47, 13, 93, 77, 100, 26, 44, 66, 73, 71, 74, 27, 6, 43, 16, 50, 7, 65, 3, 58, 7, 90, 99, 60, 84, 54, 68, 45, 28, 5, 43, 77, 47, 68, 9, 83, 66, 20, 84, 67, 4, 70, 90, 80, 11, 72, 54, 63, 9, 91, 43, 44, 36, 89, 60, 92, 70, 13, 66, 43, 45, 20, 32, 22, 61, 94, 25, 79, 27]
6 89 12 23 22 72 2 25 47 40 51 93 15 49 85 43 88 75 96 72 72 26 90 46 17 69 74 73 7 25 35 27 7 19 77 53 11 21 20 32 39 45 24 19 54 94 85 9 38 19 40 37 40 53 62 32 47 20 19 51 90 5 89 50 68 63 59 8 64 16 24 51 13 37 76 63 68 32 12 18 12 60 45 39 64
[6, 89, 12, 23, 22, 72, 2, 25, 47, 40, 51, 93, 15, 49, 85, 43, 88, 75, 96, 72, 72, 26, 90, 46, 17, 69, 74, 73, 7, 25, 35, 27, 7, 19, 77, 53, 11, 21, 20, 32, 39, 45, 24, 19, 54, 94, 85, 9, 38, 19, 40, 37, 40, 53, 62, 32, 47, 20, 19, 51, 90, 5, 89, 50, 68, 63, 59, 8, 64, 16, 24, 51, 13, 37, 76, 63, 68, 32, 12, 18, 12, 60, 45, 39, 64]
Its Correct output is:
434
"""