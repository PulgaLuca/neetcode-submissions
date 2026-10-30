class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # Calcoliamo la somma totale degli elementi dell'array
        total = sum(nums)

        # Se la somma è dispari, non è possibile dividerla
        # in due sottoinsiemi con la stessa somma
        if total % 2 != 0:
            return False

        # La somma che deve raggiungere ciascun sottoinsieme
        target = total // 2

        # Numero di elementi presenti nell'array
        n = len(nums)

        # Creiamo la matrice DP:
        # dp[i][j] indica se è possibile ottenere una somma j
        # utilizzando i primi i elementi dell'array
        #
        # Dimensioni:
        # - n + 1 righe: da 0 a n elementi
        # - target + 1 colonne: somme da 0 a target
        dp = [[False] * (target + 1) for _ in range(n + 1)]

        # Caso base:
        # È sempre possibile ottenere una somma pari a 0
        # scegliendo il sottoinsieme vuoto, indipendentemente
        # dal numero di elementi disponibili
        for i in range(n + 1):
            dp[i][0] = True

        # Consideriamo gli elementi dell'array uno alla volta
        for i in range(1, n + 1):

            # Verifichiamo tutte le somme possibili
            # da 1 fino alla somma target
            for j in range(1, target + 1):

                # Se l'elemento corrente è minore o uguale
                # alla somma che vogliamo raggiungere
                if nums[i - 1] <= j:

                    # Abbiamo due possibilità:
                    # 1. NON utilizzare l'elemento corrente:
                    #    controlliamo se potevamo già ottenere
                    #    la somma j con gli elementi precedenti.
                    #
                    # 2. UTILIZZARE l'elemento corrente:
                    #    controlliamo se con gli elementi precedenti
                    #    potevamo ottenere la somma rimanente
                    #    j - nums[i - 1].
                    #
                    # Se almeno una delle due possibilità è vera,
                    # allora possiamo ottenere la somma j.
                    dp[i][j] = dp[i - 1][j] or dp[i - 1][j - nums[i - 1]]
                else:
                    # Se l'elemento corrente è maggiore di j,
                    # non possiamo utilizzarlo.
                    # Manteniamo quindi il risultato precedente.
                    dp[i][j] = dp[i - 1][j]

        # Il risultato finale indica se è possibile ottenere
        # la somma target utilizzando tutti gli elementi.
        # Se è possibile ottenere metà della somma totale,
        # anche la parte restante avrà necessariamente
        # la stessa somma.
        return dp[n][target]