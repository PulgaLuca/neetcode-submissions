from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        if not grid:
            return
        
        rows, cols = len(grid), len(grid[0])
        queue = self.getTreasureCells(grid, rows, cols)
        self.bfs(grid, queue, rows, cols)


    def getTreasureCells(self, grid: List[List[int]], rows:int, cols:int):
        queue = deque()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    queue.append((r,c))
        
        return queue


    def isValidCell(self, r:int, c:int, grid:List[List[int]], rows:int, cols:int) -> bool:
        return 0 <= r < rows and 0 <= c < cols and grid[r][c] == 2147483647

    def bfs(self, grid:List[List[int]], queue:List, rows:int, cols:int):
        directions = [(-1,0), (1,0), (0, 1), (0,-1)]

        while queue:
            r, c = queue.popleft()

            for dr, dc in directions:
                nr, nc = r+dr, c+dc
                if not self.isValidCell(nr,nc,grid,rows,cols):
                    continue
                grid[nr][nc] = grid[r][c]+1
                queue.append((nr,nc))

    