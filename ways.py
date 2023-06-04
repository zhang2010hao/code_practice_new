

def ways(pizza, k):
    m = len(pizza)
    n = len(pizza[0])

    nums = [[0] * n for i in range(m)]

    if pizza[m - 1][n - 1] == 'A':
        nums[m - 1][n - 1] = 1

    for i in range(m - 2, -1, -1):
        if pizza[i][n - 1] == 'A':
            nums[i][n - 1] = nums[i + 1][n - 1] + 1
        else:
            nums[i][n - 1] = nums[i + 1][n - 1]

    for i in range(n - 2, -1, -1):
        if pizza[m - 1][i] == 'A':
            nums[m - 1][i] = nums[m - 1][i + 1] + 1
        else:
            nums[m - 1][i] = nums[m - 1][i + 1]

    for i in range(m - 2, -1, -1):
        for j in range(n - 2, -1, -1):
            if pizza[i][j] == 'A':
                nums[i][j] = nums[i + 1][j] + nums[i][j + 1] - nums[i + 1][j + 1] + 1
            else:
                nums[i][j] = nums[i + 1][j] + nums[i][j + 1] - nums[i + 1][j + 1]

    dp = [[[0] * n for i in range(m)] for j in range(k)]

    # k = 0
    for i in range(m):
        for j in range(n):
            if nums[i][j] > 0:
                dp[0][i][j] = 1

    # i = m - 1
    for o in range(1, k):
        for j in range(n - 2, -1, -1):
            for h in range(1, n - j):
                if nums[m - 1][j] - nums[m - 1][j + h] > 0:
                    dp[o][m - 1][j] += dp[o - 1][m - 1][j + h]


    # j = n - 1
    for o in range(1, k):
        for i in range(m - 2, -1, -1):
            for h in range(1, m - i):
                if nums[i][n - 1] - nums[i + h][n - 1] > 0:
                    dp[o][i][n - 1] += dp[o - 1][i + h][n - 1]

    # 一般
    for o in range(1, k):
        for i in range(m - 2, -1, -1):
            for j in range(n - 2, -1, -1):
                # 横切
                for h in range(1, m - i):
                    if nums[i][j] - nums[i + h][j] > 0:
                        dp[o][i][j] += dp[o - 1][i + h][j]

                # 竖切
                for h in range(1, n - j):
                    if nums[i][j] - nums[i][j + h] > 0:
                        dp[o][i][j] += dp[o - 1][i][j + h]


    mod = 1e9 + 7
    rst = int(dp[k-1][0][0] % mod)

    return rst

pizza = ["A..","AA.","..."]
k = 3
result = ways(pizza, k)
print(result)
