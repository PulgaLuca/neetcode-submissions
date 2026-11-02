class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        hold = [0] * n
        sold = [0] * n
        rest = [0] * n

        hold[0] = -prices[0]
        sold[0] = float('-inf')
        rest[0] = 0

        for i in range(1, n):
            # Come posso arrivare al giorno di oggi possedendo una moneta? 
            # due possibilità:
            # 1. Avevo già una moneta ieri e continuo a tenerla.
            # 2. Ieri ero in REST e oggi compro.
            hold[i] = max(hold[i-1], rest[i-1]-prices[i])

            # Come posso arrivare allo stato SOLD? 
            # C'è una sola possibilità: ieri possedevo una moneta e oggi la vendo.
            sold[i] = hold[i-1]+prices[i]

            # Come posso arrivare allo stato REST?
            # Ho due possibilità:
            # 1. Ero già in REST ieri.
            # 2. Ieri ero in SOLD, quindi oggi il cooldown è terminato.
            rest[i] = max(rest[i-1], sold[i-1])

        return max(sold[-1], rest[-1])