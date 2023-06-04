def spiralOrder(matrix):
    n = len(matrix)
    m = len(matrix[0])

    k = min((n + 1) // 2, (m + 1) // 2)

    visted_col = {}
    visted_row = {}

    rst = []
    for i in range(k):

        row = i
        if row not in visted_row:
            for j in range(i, m - i):
                col = j
                print('row:', row, 'col:', col)
                rst.append(matrix[row][col])

            visted_row[row] = len(visted_row)

        col = m - 1 - i
        if col not in visted_col:
            for j in range(i + 1, n - i):
                row = j
                print('row:', row, 'col:', col)
                rst.append(matrix[j][m - 1 - i])
            visted_col[col] = len(visted_col)

        row = n - 1 - i
        if row not in visted_row:
            for j in range(m - i - 2, i - 1, -1):
                col = j
                print('row:', row, 'col:', col)
                rst.append(matrix[n - 1 - i][j])
            visted_row[row] = len(visted_row)

        col = i
        if col not in visted_col:
            for j in range(n - i - 2, i, -1):
                row = j
                print('row:', row, 'col:', col)
                rst.append(matrix[j][i])
            visted_col[col] = len(visted_col)

    return rst


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(spiralOrder(matrix))
