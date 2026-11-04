# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = float('-inf')

        def dfs(node):
            nonlocal res
            if not node:
                return 0

            left_val = max(0, dfs(node.left))
            right_val = max(0, dfs(node.right))

            res = max(res, node.val + left_val + right_val)

            return node.val + max(left_val, right_val)

        dfs(root)
        return res