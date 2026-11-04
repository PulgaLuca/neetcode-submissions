# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    '''
    queue = [1] -> [2, -1]
    current = -1
            1       (max_val,1)
          /   \
        2      -1   (max_val, 2) (max_val, 1)
       / \
      3   4         (max_val, 3 - max_val, 4) 
    good_nodes = 1
    '''
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        good_nodes = 0
        stack = [(root, float('-inf'))]

        while stack:
            current, max_val = stack.pop()

            if current.val >= max_val:
                good_nodes += 1
            
            max_val = max(max_val, current.val)

            if current.left: stack.append((current.left, max_val))
            if current.right: stack.append((current.right, max_val))

        return good_nodes

