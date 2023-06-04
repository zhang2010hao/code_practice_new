def longestIncreasingPath(matrix):
    m, n = len(matrix), len(matrix[0])
    dp1 = [[1] * n for _ in range(m)]
    dp2 = [[1] * n for _ in range(m)]

    max_len = 1
    for i in range(1, m):
        if matrix[i][0] < matrix[i - 1][0]:
            dp1[i][0] = dp1[i - 1][0] + 1

        if matrix[i][0] > matrix[i - 1][0]:
            dp2[i][0] = dp2[i - 1][0] + 1

        max_len = max(max_len, dp1[i][0], dp2[i][0])

    for i in range(1, n):
        if matrix[0][i] < matrix[0][i - 1]:
            dp1[0][i] = dp1[0][i - 1] + 1

        if matrix[0][i] > matrix[0][i - 1]:
            dp2[0][i] = dp2[0][i - 1] + 1

        max_len = max(max_len, dp1[0][i], dp2[0][i])

    for i in range(1, m):
        for j in range(1, n):
            t1 = 1
            if matrix[i][j] < matrix[i][j - 1]:
                t1 = dp1[i][j - 1] + 1
            t2 = 1
            if matrix[i][j] < matrix[i - 1][j]:
                t2 = dp1[i - 1][j] + 1

            dp1[i][j] = max(t1, t2)

            t1 = 1
            if matrix[i][j] > matrix[i][j - 1]:
                t1 = dp2[i][j - 1] + 1
            t2 = 1
            if matrix[i][j] > matrix[i - 1][j]:
                t2 = dp2[i - 1][j] + 1

            dp2[i][j] = max(t1, t2)

            max_len = max(max_len, dp1[i][j], dp2[i][j])

    return max_len


matrix = [[7,8,9],[9,7,6],[7,2,3]]
print(longestIncreasingPath(matrix))
