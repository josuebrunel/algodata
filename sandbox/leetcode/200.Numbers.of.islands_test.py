def isIsland(i, j, grid, visited):
    # if water
    if grid[i][j] == "0":
        visited[i][j] = 2
        return 0

    # if neighbor in exploration
    if grid[i][j] == "1" and visited[i][j] != 0:
        return 0

    visited[i][j] = 1
    neighbors = [[0, -1], [0, 1], [-1, 0], [1, 0]]
    for n in neighbors:
        x = n[0] + i
        y = n[1] + j

        if not (0 <= x < len(grid)):
            continue
        if not (0 <= y < len(grid[i])):
            continue

        isIsland(x, y, grid, visited)

    visited[i][j] = 2
    return 1

def numIsland(grid):
    visited = [[0 for _ in i] for i in grid]
    num = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            num += isIsland(i, j, grid, visited)
    return num


if __name__ == "__main__":
    grid = [
            ["1","1","1","1","0"],
            ["1","1","0","1","0"],
            ["1","1","0","0","0"],
            ["0","0","0","0","0"]
    ]
    assert numIsland(grid) == 1
    grid = [
            ["1","1","0","0","0"],
            ["1","1","0","0","0"],
            ["0","0","1","0","0"],
            ["0","0","0","1","1"]
    ]
    assert numIsland(grid) == 3
