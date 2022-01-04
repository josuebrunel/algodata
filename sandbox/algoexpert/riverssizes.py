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


