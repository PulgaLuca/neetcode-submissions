from collections import deque

class Solution:
    # O(n*m) O(n*m)
    SAFE = "S"
    DIRECTIONS = [(1,0),(-1,0),(0,1),(0,-1)]

    def solve(self, board: List[List[str]]) -> None:
        if not board:
            return
        
        rows, cols = len(board), len(board[0])
        safeCellsQueue = self.checkSafeCells(rows, cols, board)
        self.makeSafeRegions(rows, cols, board, safeCellsQueue)
        self.markSurroundedRegions(rows, cols, board)

    def isBorder(self,r:int, c:int, rows:int, cols:int) -> bool:
        return r == 0 or c == 0 or r == rows-1 or c == cols-1

    def isValidOCell(self,r:int,c:int,rows:int,cols:int,board:List[List[int]]):
        return 0 <= r < rows and 0 <= c < cols and board[r][c] == "O"

    def checkSafeCells(self,rows:int, cols:int, board:List[List[int]]) -> Deque[Tuple[int,int]]:
        queue = deque()
        for r in range(rows):
            for c in range(cols):
                if self.isBorder(r,c,rows,cols) and board[r][c] == "O":
                    board[r][c] = self.SAFE
                    queue.append((r,c))
        return queue

    def makeSafeRegions(self,rows:int,cols:int,board:List[List[int]], safeCellsQueue: Deque[Tuple[int,int]]):
        while safeCellsQueue:
            r,c = safeCellsQueue.popleft()
            for dr, dc in self.DIRECTIONS:
                nr,nc = dr+r, dc+c
                if not self.isValidOCell(nr,nc,rows,cols,board):
                    continue
                board[nr][nc] = self.SAFE
                safeCellsQueue.append((nr,nc))


    def markSurroundedRegions(self,rows:int,cols:int,board:List[List[int]]):
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O":
                    board[r][c] = "X"
                if board[r][c] == self.SAFE:
                    board[r][c] = "O"
        