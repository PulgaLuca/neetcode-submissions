# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    '''
    recursive style
    '''
    def goodNodes(self, root: TreeNode) -> int:
        return self.dfs(root, float('-inf'))

    def dfs(self, root: TreeNode, max_val: int):
        if not root:
            return 0
        
        good_nodes = 0

        if root.val >= max_val:
            good_nodes = 1
        
        max_val = max(max_val, root.val)

        good_nodes += self.dfs(root.left, max_val)
        good_nodes += self.dfs(root.right, max_val)

        return good_nodes
