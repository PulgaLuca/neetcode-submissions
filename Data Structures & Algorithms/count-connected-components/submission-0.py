class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n
    
    def find(self, node):
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]

    def union(self, u, v):
        pu = self.find(u)
        pv = self.find(v)
        if pu == pv:
            return False
        if self.size[pu] >= self.size[pv]:
            self.parent[pv] = pu
            self.size[pu] += self.size[pv]
        else:
            self.parent[pu] = pv
            self.size[pv] += self.size[pu]
        return True

    def connected(self, u, v):
        return self.find(u) == self.find(v)

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        dsu = DSU(n)
        res = n
        for u, v in edges:
            if dsu.union(u,v):
                res -= 1
        return res