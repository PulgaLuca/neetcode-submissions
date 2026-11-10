class DSU:
    def __init__(self, n):
        self.parent = list(range(n+1))
        self.size = [1] * (n+1)

    def find(self, node):
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x == root_y:
            return False

        if self.size[root_x] < self.size[root_y]:
            root_x, root_y = root_y, root_x

        self.parent[root_y] = root_x
        self.size[root_x] += self.size[root_y]
        return True

class Solution:
    
    def checkValidPos(self, nr, nc, rows, cols, grid):
        if (nr < 0 or nc < 0 or nr >= rows or nc >= cols or grid[nr][nc] == "0"):
            return True
        return False

    # needed to convert the DSU in matrix-array format identifier
    def index(self, r, cols, c):
        return r*cols+c
        
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        islands = 0
        dsu = DSU(rows*cols)
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    islands+=1
                    for dr, dc in directions:
                        nr, nc = r+dr, c+dc
                        if self.checkValidPos(nr, nc, rows, cols, grid):
                            continue
                        
                        if dsu.union(self.index(r,cols, c), self.index(nr,cols,nc)):
                            islands -= 1

        return islands
    
    
    
