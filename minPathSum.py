def minPathSum(grid):
    m = len(grid)
    n = len(grid[0])
    dp = [[0] * n for i in range(m)]
    dp[0][0] = grid[0][0]

    for i in range(m):
        for j in range(n):
            minv = 10000
            if i - 1 >= 0:
                minv = min(minv, dp[i - 1][j])

            if j - 1 >= 0:
                minv = min(minv, dp[i][j - 1])

            if minv != 10000:
                dp[i][j] = minv + grid[i][j]


    return dp[m-1][n-1]

grid = [[1,3,1],[1,5,1],[4,2,1]]
print(minPathSum(grid))