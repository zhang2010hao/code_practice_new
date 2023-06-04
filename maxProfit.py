
def maxProfit(prices):
    max_profit = 0
    min_price = prices[0]

    for i in range(1, len(prices)):
        max_profit = max(max_profit, prices[i] - min_price)
        min_price = min(min_price, prices[i])

    return max_profit