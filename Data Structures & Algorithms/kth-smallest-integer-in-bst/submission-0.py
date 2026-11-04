# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.right = right
        self.left = left

'''
root = TreeNode(5)

root.left = TreeNode(3)
root.right = TreeNode(8)

Possible extension:
root.right.left = TreeNode(6)
root.right.right = TreeNode(9)

Since BST is already "sorted" in some kind of way, from left to right
Inorder traversal
'''
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        arr = []

        def dfs(node):
            if not node:
                return
            dfs(node.left)
            arr.append(node.val)
            dfs(node.right)

        dfs(root)
        return arr[k-1]
        