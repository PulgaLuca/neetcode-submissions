# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        '''
        Il nodo 1 riceverà -1 dal figlio e propagherà immediatamente il risultato.
        La funzione restituisce quindi:
        Un numero positivo o zero → altezza del sottoalbero, se bilanciato.
        -1 → sottoalbero non bilanciato.
        '''
        def dfs(root):
            if not root:
                return 0
            
            left_depth = dfs(root.left)
            right_depth = dfs(root.right)
            
            # Sentinel value (-1) con early return (sentinel value propagration)
            if left_depth == -1 or right_depth == -1:
                return -1

            if abs(left_depth-right_depth) > 1:
                return -1

            return 1+max(left_depth, right_depth)
        return dfs(root) != -1