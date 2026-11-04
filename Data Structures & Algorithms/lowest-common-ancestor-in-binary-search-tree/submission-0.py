# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        def find_lca(node):
            if not node or node is p or node is q:
                return node
            
            left_child = find_lca(node.left)
            right_child = find_lca(node.right)
        
            # If both recursive calls return a non-None value, it means:
            # One target was found in the left subtree.
            # The other target was found in the right subtree.
            #Therefore, the current node is their Lowest Common Ancestor.
            if left_child and right_child:
                return node
            
            # parent propagation
            if left_child: return left_child
            if right_child: return right_child
            return None

        return find_lca(root)
