
def minDistance(word1, word2):
    n = len(word1)
    m = len(word2)

    if n * m == 0:
        return n + m

    # 因为第0行和第0列是空字符串像非空字符串转移
    dp = [[0] * (m+1) for _ in range(n+1)]
    for i in range(n+1):
        dp[i][0] = i

    for i in range(m+1):
        dp[0][i] = i

    for i in range(1, n+1):
        for j in range(1, m+1):
            if word1[i-1] == word2[j-1]:
                min_v = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1] - 1)
                dp[i][j] = 1 + min_v
            else:
                min_v = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])
                dp[i][j] = 1 + min_v

    return dp[n][m]