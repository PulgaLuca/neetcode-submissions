# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.dfs(root, float('-inf'), float('inf'))

    def dfs(self, root: Optional[TreeNode], left_upper_bound: int, right_upper_bound: int) -> bool:
        if not root:
            return True
        
        if not left_upper_bound < root.val < right_upper_bound:
            return False
        
        return self.dfs(root.left, left_upper_bound, root.val) and self.dfs(root.right, root.val, right_upper_bound)
