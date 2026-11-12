class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        visited = set()
        rows = len(grid)
        cols = len(grid[0])
        max_area, curr_area = 0, 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r,c) not in visited:
                    curr_area = self.exploreDfs(r, c, grid, visited)
                    max_area = max(curr_area, max_area)
        return max_area

    def checkValidIslandCell(self, r:int, c:int, grid:List[List[int]]) -> bool:
        n_rows = len(grid)
        n_cols = len(grid[0])

        if r < 0 or c < 0 or r >= n_rows or c >= n_cols:
            return False
        return grid[r][c] == 1
    
    def exploreDfs(self, r:int, c:int, grid: List[List[int]], visited:set) -> int:
        if not self.checkValidIslandCell(r,c,grid):
            return 0
        
        if (r,c) in visited:
            return 0

        visited.add((r,c))

        curr_area = 1

        curr_area+=self.exploreDfs(r+1,c,grid,visited)
        curr_area+=self.exploreDfs(r-1,c,grid,visited)
        curr_area+=self.exploreDfs(r,c+1,grid,visited)
        curr_area+=self.exploreDfs(r,c-1,grid,visited)

        return curr_area
