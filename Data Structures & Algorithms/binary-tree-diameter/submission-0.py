# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        diameter = 0 # global reference we want to maximize
        def dfs(root):
            nonlocal diameter
                
            if not root:
                return 0
            # classic dfs traversal
            left_depth = dfs(root.left)
            right_depth = dfs(root.right)
            # global reference we want to maximize
            diameter = max(diameter, left_depth+right_depth)
            # parent node needed information
            return 1+max(right_depth, left_depth)

        dfs(root)
        return diameter