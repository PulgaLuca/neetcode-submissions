from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        queue, fresh = self.getInitialState(rows, cols, grid)

        minutes, fresh = self.bfs(grid, rows, cols, queue, fresh)

        return minutes if fresh == 0 else -1

    def getInitialState(self, rows, cols, grid):
        queue = deque()
        fresh = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r, c))
                elif grid[r][c] == 1:
                    fresh += 1

        return queue, fresh

    def isValidFreshCell(self, r, c, rows, cols, grid):
        return (
            0 <= r < rows
            and 0 <= c < cols
            and grid[r][c] == 1
        )

    def bfs(self, grid, rows, cols, queue, fresh):
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        minutes = 0

        while queue and fresh > 0:
            for _ in range(len(queue)):
                r, c = queue.popleft()

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc

                    if not self.isValidFreshCell(nr, nc, rows, cols, grid):
                        continue

                    grid[nr][nc] = 2
                    fresh -= 1
                    queue.append((nr, nc))

            minutes += 1

        return minutes, fresh