
def coinChange(coins, amount):

    dp = [float('inf')] * (amount + 1)
    dp[0] = 0

    for coin in coins:
        for i in range(coin, amount):
            dp[i] = min(dp[i], dp[i-coin]) + 1

    if dp[-1] != float('inf'):
        return dp[-1]
    else:
        return -1
