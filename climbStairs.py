

def climbStairs(n):
    dp = [0] * n
    if n == 1:
        return 1
    elif n == 2:
        return 2

    dp[0] = 1
    dp[1] = 2



    for i in range(2, n):
        dp[i] = dp[i-1] + dp[i-2]

    return dp[n-1]
