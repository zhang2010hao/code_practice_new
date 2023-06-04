def numIslands(grid):
    def bfs(arr):
        nr = len(arr)
        if nr < 1:
            return 0
        nc = len(arr[0])

        nisland = 0
        for i in range(nr):
            for j in range(nc):
                if arr[i][j] == '1':
                    nisland += 1
                    neibors = [(i, j)]

                    while len(neibors) > 0:
                        row, col = neibors.pop(0)
                        arr[row][col] = '0'
                        for k, l in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
                            if row + k >= 0 and row + k < nr and col + l >= 0 and col + l < nc and arr[row + k][
                                col + l] == '1':
                                neibors.append((row + k, col + l))
                                arr[row + k][col + l] = '0'
        return nisland

    # def dfs(row, col):
    #     grid[row][col] = '0'
    #     for k, l in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
    #             if row + k >= 0 and row + k < nr and col + l >= 0 and col + l < nc and grid[row + k][col + l] == '1':
    #                 dfs(row + k, col + l)
    #
    # nr = len(grid)
    # if nr < 1:
    #     return 0
    # nc = len(grid[0])
    #
    # nisland = 0
    # for i in range(nr):
    #     for j in range(nc):
    #         if grid[i][j] == '1':
    #             nisland += 1
    #             dfs(i, j)
    nisland = bfs(grid)

    return nisland


grid = [["1", "1", "1", "1", "1", "0", "1", "1", "1", "1", "1", "1", "1", "1", "1", "0", "1", "0", "1", "1"],
        ["0", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "0", "1", "1", "1", "1", "1", "0"],
        ["1", "0", "1", "1", "1", "0", "0", "1", "1", "0", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1"],
        ["1", "1", "1", "1", "0", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1"],
        ["1", "0", "0", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1"],
        ["1", "0", "1", "1", "1", "1", "1", "1", "0", "1", "1", "1", "0", "1", "1", "1", "0", "1", "1", "1"],
        ["0", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "0", "1", "1", "0", "1", "1", "1", "1"],
        ["1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "0", "1", "1", "1", "1", "0", "1", "1"],
        ["1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "0", "1", "1", "1", "1", "1", "1", "1", "1", "1"],
        ["1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1"],
        ["0", "1", "1", "1", "1", "1", "1", "1", "0", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1"],
        ["1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1"],
        ["1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1"],
        ["1", "1", "1", "1", "1", "0", "1", "1", "1", "1", "1", "1", "1", "0", "1", "1", "1", "1", "1", "1"],
        ["1", "0", "1", "1", "1", "1", "1", "0", "1", "1", "1", "0", "1", "1", "1", "1", "0", "1", "1", "1"],
        ["1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "0", "1", "1", "1", "1", "1", "1", "0"],
        ["1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "0", "1", "1", "1", "1", "0", "0"],
        ["1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1"],
        ["1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1"],
        ["1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1"]]

print(numIslands(grid))