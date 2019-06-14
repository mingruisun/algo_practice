import utils
logging_run_time = utils.program_run_time()


coin_bag_1 = (4, [1, 2, 3])
coin_bag_2 = (10, [2, 5, 3, 6])

def coin_change_naive(change, nth_coin, coin_bag):
    if change == 0:
        return 1
    if change < 0:
        return 0
    if nth_coin < 0 and change > 0:
        return 0
    return coin_change_naive(change - coin_bag[nth_coin], nth_coin, coin_bag) + coin_change_naive(change, nth_coin - 1, coin_bag)

def coin_change_towndown_dp_helper(change, nth_coin, coin_bag, dp):
    if change == 0:
        return 1
    if change < 0:
        return 0
    if nth_coin < 0 and change > 0:
        return 0
    if dp[nth_coin][change] == -1:
        dp[nth_coin][change] = coin_change_naive(change - coin_bag[nth_coin], nth_coin, coin_bag) + coin_change_naive(change, nth_coin - 1, coin_bag)
    return dp[nth_coin][change]

def coin_change_topdown_dp(change, coin_bag):
    dp = [[-1 for x in range(0, change + 1)] for y in range(0, len(coin_bag) + 1)]
    return coin_change_towndown_dp_helper(change, len(coin_bag) - 1, coin_bag, dp)


logging_run_time.reset_start_time()
print(coin_change_naive(coin_bag_1[0], len(coin_bag_1[1]) - 1, coin_bag_1[1]))
logging_run_time.report_total_runtime("Naive method")

logging_run_time.reset_start_time()
print(coin_change_topdown_dp(coin_bag_1[0], coin_bag_1[1]))
logging_run_time.report_total_runtime("Topdown DP")

# print(coin_change_naive(coin_bag_2[0], len(coin_bag_2[1]) - 1, coin_bag_2[1]))

# print(coin_change_topdown_dp(coin_bag_1[0], coin_bag_1[1]))
# print(coin_change_topdown_dp(coin_bag_2[0], coin_bag_2[1]))