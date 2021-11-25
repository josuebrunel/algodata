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

