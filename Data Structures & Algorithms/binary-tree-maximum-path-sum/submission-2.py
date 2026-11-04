# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

'''
La DFS fa questo:
Scende ricorsivamente fino alle foglie.
Calcola il guadagno del figlio sinistro.
Calcola il guadagno del figlio destro.
Aggiorna il massimo globale usando entrambi i figli.
Restituisce al genitore il valore usando solo il figlio migliore.

res = miglior percorso che può passare attraverso il nodo, usando entrambi i figli.
return = miglior percorso che può essere esteso dal genitore, usando un solo figlio.
'''
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        # Variabile che mantiene il massimo path sum trovato
        # float('-inf') perché anche tutti i nodi potrebbero essere negativi
        res = float('-inf')

        # Funzione ricorsiva che calcola il massimo guadagno
        # ottenibile partendo da un nodo e andando verso il basso
        def dfs(node):

            # Permette alla funzione interna di modificare
            # la variabile res definita nella funzione esterna
            nonlocal res

            # Caso base: se il nodo non esiste,
            # non contribuisce al path sum
            if not node:
                return 0

            # Calcoliamo il massimo guadagno del sottoalbero sinistro
            # Se è negativo, lo ignoriamo (prendiamo 0)
            left_val = max(0, dfs(node.left))

            # Calcoliamo il massimo guadagno del sottoalbero destro
            # Anche qui ignoriamo eventuali valori negativi
            right_val = max(0, dfs(node.right))

            # Consideriamo un percorso che passa per il nodo corrente
            # Possiamo utilizzare ENTRAMBI i figli:
            # sinistro + nodo corrente + destro
            #
            # Aggiorniamo il massimo globale se troviamo
            # un percorso migliore
            res = max(res, node.val + left_val + right_val)

            # Restituiamo al genitore il massimo guadagno possibile
            # Possiamo scegliere SOLO uno dei due figli,
            # perché il percorso non può biforcarsi
            return node.val + max(left_val, right_val)

        # Avviamo la ricorsione partendo dalla radice
        dfs(root)

        # Restituiamo il massimo path sum trovato
        return res

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