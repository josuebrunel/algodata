#### [ graphs.py ]( graphs.py )

```python

grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]



class Graph(object):

    def __init__(self, grid):
        self.grid = grid

    def traverse(self):
        visited = []
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                visited.append(grid[i][j])
        return visited

    def neighbors(self, i, j):
        directions = [
            [0, -1], # left
            [0, 1], # right
            [-1, 0], # up
            [1, 0] # down
        ]
        neighbors = []
        for d in directions:
            x = d[0] + i
            y = d[1] + j
            if not (0 <= x < len(self.grid)):
                continue
            if not (0 <= y < len(self.grid[i])):
                continue
            neighbors.append((x, y))
        return neighbors


graph = Graph(grid)



```



#### [ numberofislands.py ]( numberofislands.py )

```python

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


```



#### [ riverssizes.py ]( riverssizes.py )

```python

grid = [
  [1, 0, 0, 1, 0],
  [1, 0, 1, 0, 0],
  [0, 0, 1, 0, 1],
  [1, 0, 1, 0, 1],
  [1, 0, 1, 1, 0]
]

def rivers_sizes(grid):
    sizes = []
    visited = [[False for _ in i] for i in grid]
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 0 or visited[i][j]:
                continue
            sizes.append(get_size(i, j, grid, visited))
    return sizes


def get_size(i, j, grid, visited):
    visited[i][j] = True
    size = 1
    directions = [[0, -1], [0, 1], [-1, 0], [1, 0]]
    for d in directions:
        x = d[0] + i
        y = d[1] + j

        if not (0 <= x < len(grid)):
            continue
        if not (0 <= y < len(grid[i])):
            continue

        if grid[x][y] == 0 or visited[x][y]:
            continue
        size += get_size(x, y, grid, visited)
    return size


if __name__ == "__main__":
    print(rivers_sizes(grid))




```



