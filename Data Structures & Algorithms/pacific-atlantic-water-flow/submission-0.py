
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights:
            return []

        rows, cols = len(heights), len(heights[0])

        pacific = self.getReachableCells(heights, rows, cols, True)
        atlantic = self.getReachableCells(heights, rows, cols, False)

        return [[r, c] for r, c in pacific & atlantic]

    def getReachableCells(self, heights, rows, cols, pacific):
        visited = set()
        
        for r in range(rows):
            for c in range(cols):
                isBorder = (
                    r == 0 or c == 0
                    if pacific
                    else r == rows - 1 or c == cols - 1
                )

                if isBorder:
                    self.dfs(r, c, heights, visited, rows, cols)

        return visited

    def dfs(self, r, c, heights, visited, rows, cols):
        if (r, c) in visited:
            return

        visited.add((r, c))

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        for dr, dc in directions:
            nr, nc = r + dr, c + dc

            if not self.isValidCell(nr, nc, r, c, heights, rows, cols):
                continue

            self.dfs(nr, nc, heights, visited, rows, cols)

    def isValidCell(self, nr, nc, r, c, heights, rows, cols):
        return (
            0 <= nr < rows
            and 0 <= nc < cols
            and heights[nr][nc] >= heights[r][c]
        )
