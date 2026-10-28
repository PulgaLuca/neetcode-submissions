class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        
        res = 0
        n=len(height)
        l, r = 0, n-1
        leftmax, rightmax = height[l], height[r]

        while l < r:
            #Non hai bisogno di conoscere il massimo esatto a destra: sai già che è almeno 4, quindi non può essere il limite che impedisce all'acqua di salire fino a 3.

            if leftmax < rightmax:
                l+=1
                leftmax = max(leftmax, height[l])
                res += leftmax - height[l]
            else:
                # Non puoi essere certo di quanta acqua ci sia nella prossima posizione a sinistra, perché il limite potrebbe dipendere dal muro destro, che è più basso. Invece, puoi calcolare con certezza l'acqua sul lato destro, perché il muro sinistro è già alto 5 e supera quello destro.
                r-=1
                rightmax=max(rightmax, height[r])
                res += rightmax - height[r]

        return res
