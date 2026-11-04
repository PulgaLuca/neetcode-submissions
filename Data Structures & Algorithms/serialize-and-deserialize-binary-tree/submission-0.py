# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        def dfs(node):
            if not node: 
                return ['N']
            return [str(node.val)] + dfs(node.left) + dfs(node.right)
        return ','.join(dfs(root))
        
     # Ricostruisce l'albero dalla stringa
    def deserialize(self, data: str) -> Optional[TreeNode]:
        # Convertiamo la stringa in una lista di valori
        # Esempio: "1,2,N,N,3,N,N" -> ['1','2','N','N','3','N','N']
        vals = iter(data.split(','))

        def dfs():
            # Prendiamo il prossimo valore disponibile
            val = next(vals)
            # Se troviamo N, significa che il nodo è None
            if val == 'N':
                return None

            # Creiamo un nuovo nodo con il valore letto
            node = TreeNode(int(val))
            # Ricostruiamo ricorsivamente il figlio sinistro
            node.left = dfs()
            # Ricostruiamo ricorsivamente il figlio destro
            node.right = dfs()
            # Restituiamo il nodo completo
            return node

        # Iniziamo la ricostruzione dalla radice
        return dfs()