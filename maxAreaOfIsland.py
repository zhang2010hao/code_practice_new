def maxAreaOfIsland(grid):
    def bfs(arr):
        nr = len(arr)
        if nr < 1:
            return 0
        nc = len(arr[0])

        max_island = 0
        for i in range(nr):
            for j in range(nc):
                if arr[i][j] == 1:
                    v_island = 1
                    neibors = [(i, j)]
                    while len(neibors) > 0:
                        row, col = neibors.pop(0)
                        arr[row][col] = 0
                        for k, l in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
                            if row + k >= 0 and row + k < nr and col + l >= 0 and col + l < nc and arr[row + k][
                                col + l] == 1:
                                v_island += 1
                                neibors.append((row + k, col + l))
                                arr[row + k][col + l] = 0
                    max_island = max(max_island, v_island)

        return max_island

    return bfs(grid)


grid = [[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
        [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
        [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]

print(maxAreaOfIsland(grid))
