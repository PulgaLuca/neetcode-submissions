class Solution:
    def checkValidIslandCell(self, r, c, grid) -> bool:
        rows = len(grid)
        cols = len(grid[0])
        if r < 0 or c < 0 or r >= rows or c >= cols:
            return False
        
        return grid[r][c] == "1"

    def explore(self, grid: List[List[str]], r:int, c:int, visited: Set) -> bool:
        if not self.checkValidIslandCell(r, c, grid):
            return False

        if (r,c) in visited:
            return False

        visited.add((r,c))

        self.explore(grid, r+1, c, visited)
        self.explore(grid, r-1, c, visited)
        self.explore(grid, r, c+1, visited)
        self.explore(grid, r, c-1, visited)
        return True
    
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        visited = set()
        rows = len(grid)
        cols = len(grid[0])
        islands = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r,c) not in visited:
                    islands += 1
                    self.explore(grid, r, c, visited)
            

        return islands


