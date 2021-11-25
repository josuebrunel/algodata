grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]

LAND = "1"
WATER = "0"

def numIslands(grid):
    visited = [[False for _ in i] for i in grid]
    num = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == WATER or visited[i][j]:
                continue
            num += isIsland(i, j, grid, visited)
    return num


def isIsland(i, j, grid, visited):
    visited[i][j] = True
    num = 1
    directions = [[0, -1], [0, 1], [-1, 0], [1, 0]]
    for dr in directions:
        x = dr[0] + i
        y = dr[1] + j
        if not (0 <= x < len(grid)):
            continue
        if not (0 <= y < len(grid[i])):
            continue
        if grid[i][j] == WATER or visited[x][y]:
            continue
        
    return num

if __name__ == "__main__":
    print(numIslands(grid))
