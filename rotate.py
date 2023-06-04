def rotate(matrix):
    # n = len(matrix)
    # for i in range(n // 2):
    #     for j in range((n + 1) // 2):
    #         tmp = matrix[i][j]
    #         matrix[i][j] = matrix[n - j - 1][i]
    #         matrix[n - j - 1][i] = matrix[n - i - 1][n - j - 1]
    #         matrix[n - i - 1][n - j - 1] = matrix[j][n - i - 1]
    #         matrix[j][n - i - 1] = tmp

    n = len(matrix)
    # 先沿着行中间对折
    k = n // 2
    for i in range(k):
        for j in range(n):
            matrix[i][j], matrix[n-1-i][j] = matrix[n-1-i][j], matrix[i][j]

    # 再沿着对角线对折
    for i in range(n):
        for j in range(i):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

