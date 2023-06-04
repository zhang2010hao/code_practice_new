def maximalSquare(matrix):
    n = len(matrix)
    m = len(matrix[0])

    max_num = 0
    dp = [[0] * m for i in range(n)]
    for i in range(n):
        if matrix[i][0] == '1':
            dp[i][0] = 1
            max_num = 1

    for i in range(m):
        if matrix[0][i] == '1':
            dp[0][i] = 1
            max_num = 1

    for r in range(1, n):
        for c in range(1, m):
            # if dp[r - 1][c - 1] == 0:
            #     if matrix[r][c] == '1':
            #         dp[r][c] = 1
            # else:
            #     flag = True
            #     idx = 0
            #     for j in range(dp[r - 1][c - 1] + 1):
            #         idx = j
            #         if matrix[r][c - j] != '1' or matrix[r - j][c] != '1':
            #             flag = False
            #             break
            #     if flag:
            #         dp[r][c] = dp[r - 1][c - 1] + 1
            #     elif matrix[r][c] == '1':
            #         dp[r][c] = 1 + idx - 1
            #
            # max_num = max(max_num, dp[r][c])
            if matrix[r][c] == '1':
                dp[r][c] = min(dp[r - 1][c], dp[r][c - 1]) + 1

            max_num = max(max_num, dp[r][c])

    return max_num * max_num


matrix = [["1", "0", "1", "0"],
          ["1", "0", "1", "1"],
          ["1", "0", "1", "1"],
          ["1", "1", "1", "1"]]
print(maximalSquare(matrix))
