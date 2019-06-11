import utils
logging_run_time = utils.program_run_time()


gold_mine_1 = [
    [1, 3, 3],
    [2, 1, 4],
    [0, 6, 4]
]

# Output : 12
# {(1,0)->(2,1)->(2,2)}


gold_mine_2 = [
    [1, 3, 1, 5],
    [2, 2, 4, 1],
    [5, 0, 2, 3],
    [0, 6, 1, 2]
]

# Output : 16
# (2,0) -> (1,1) -> (1,2) -> (0,3) OR
# (2,0) -> (3,1) -> (2,2) -> (2,3)


gold_mine_3 = [
    [10, 33, 13, 15],
    [22, 21, 4, 1],
    [5, 0, 2, 3],
    [0, 6, 14, 2]
]

# Output : 83
#

gold_mine_4 = [
    [77, 15, 93, 35, 86, 92, 49],
     [21, 62, 27, 90, 59, 63, 26],
     [40, 26, 72, 36, 11, 68, 67],
     [29, 82, 30, 62, 23, 67, 35]
    ]

# output: 549

gold_mine_5 = [[22, 58, 69],
 [67, 93, 56],
 [11, 42, 29],
 [73, 21, 19],
 [84, 37, 98],
 [24, 15, 70],
 [13, 26, 91],
 [80, 56, 73],
 [62, 70, 96],
 [81, 5, 25]]

# output: 247


def gold_mine(mat):
    y = len(mat) - 1
    x = len(mat[0]) - 1

    res = []
    for i in range(0, y + 1):
        res.append(gold_mine_naive(mat, x, i))
    return max(res)

def gold_mine_naive(gold_mine, x, y):

    if x < 0 or y < 0:
        return 0
    max_y = len(gold_mine) - 1
    max_x = len(gold_mine[0]) - 1

    if x > max_x or y > max_y:
        return 0

    return gold_mine[y][x] + max(gold_mine_naive(gold_mine, x - 1, y + 1), gold_mine_naive(gold_mine, x - 1, y), gold_mine_naive(gold_mine, x - 1, y - 1))


def gold_mine_topdown_dp_helper(gold_mine, x, y, dp):
    if x < 0 or y < 0:
        return 0
    max_y = len(gold_mine) - 1
    max_x = len(gold_mine[0]) - 1

    if x > max_x or y > max_y:
        return 0
    if dp[y][x] == -1:
        temp_max_gold = gold_mine[y][x] + max(gold_mine_topdown_dp_helper(gold_mine, x - 1, y + 1, dp), gold_mine_topdown_dp_helper(gold_mine, x - 1, y, dp), gold_mine_topdown_dp_helper(gold_mine, x - 1, y - 1, dp))
        dp[y][x] = temp_max_gold
    return dp[y][x]

def gold_mine_topdown_dp(gold_mine):
    dp = [[-1 for i in range(len(gold_mine[0]))] for j in range(len(gold_mine))]

    y = len(gold_mine) - 1
    x = len(gold_mine[0]) - 1

    res = []
    for i in range(0, y + 1):
        res.append(gold_mine_topdown_dp_helper(gold_mine, x, i, dp))
    return max(res)

def gold_mine_bottomup_dp(gold_mine):

#    loop through columns starting from column 1 until the end
#       loop through each row, calculate the temporary max from previous column, store the values in dp

    max_y = len(gold_mine) - 1
    dp = [[-1 for i in range(len(gold_mine[0]))] for j in range(len(gold_mine))]

    for i in range(len(gold_mine)):
        dp[i][0] = gold_mine[i][0]

    for x in range(1, len(gold_mine[0])):
        right = 0
        top_right = 0
        bottom_right = 0

        for y in range(0, len(gold_mine)):
#           if going top-right from previous column
            if y == 0:
                top_right = 0
            else:
                top_right = dp[y - 1][x - 1]

#           if going right from previous column
            right = dp[y][x - 1]

#           if going bottom-right from previous column
            if y == max_y:
                bottom_right = 0
            else:
                bottom_right = dp[y + 1][x - 1]

            dp[y][x] = gold_mine[y][x] + max(top_right, right, bottom_right)

    temp_max = dp[0][-1]
    for i in range(1, len(dp)):
        if dp[i][-1] > temp_max:
            temp_max = dp[i][-1]

    # print(dp)
    return temp_max



logging_run_time.reset_start_time()
print(gold_mine(gold_mine_4))
logging_run_time.report_total_runtime("Naive method")

logging_run_time.reset_start_time()
print(gold_mine_topdown_dp(gold_mine_4))
logging_run_time.report_total_runtime("Topdown DP method")

logging_run_time.reset_start_time()
print(gold_mine_bottomup_dp(gold_mine_5))
logging_run_time.report_total_runtime("BottomUp DP method")



''' driver program

for t in range(int(input())):
    [row, col] = [int(x) for x in input().split()]
    gold_list = [int(x) for x in input().split()]
    gold_mine = [[-1 for x in range(col)] for y in range(row)]
    for j in range(row):
        for i in range(col):
            gold_mine[j][i] = gold_list[col*j + i]
    print(gold_mine_bottomup_dp(gold_mine))
'''