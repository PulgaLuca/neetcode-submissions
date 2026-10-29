class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # brute force approach O(m+n) in which m=n.rows, n=n.cols
        rows, columns = len(matrix), len(matrix[0])
        r, c = 0, columns-1

        while r < rows and c >= 0:
            if matrix[r][c] > target:
                c-=1
            elif matrix[r][c] < target:
                r+=1
            else:
                return True
        
        return False