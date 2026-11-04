# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        stack = [(root, float('-inf'), float('inf'))]

        while stack:
            node, left_val, right_val = stack.pop()

            if not left_val < node.val < right_val:
                return False
            
            if node.left:
                stack.append((node.left, left_val, node.val))
            if node.right:
                stack.append((node.right, node.val, right_val))

        return True
