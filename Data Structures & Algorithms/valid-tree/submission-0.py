class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if n <= 0 or len(edges) != n-1:
            return False
        visited = set()
        graph = self.buildGraph(n, edges)
        self.iterativeDfs(0, graph, visited)
        return len(visited) == n
    
    def buildGraph(self, n:int, edges: List[List[int]]):
        graph = [[] for _ in range(n)]
        for parent, node in edges:
            graph[parent].append(node)
            graph[node].append(parent)
        return graph
    
    def iterativeDfs(self, node, graph, visited):
        stack = [node]
        visited.add(node)
        while stack:
            node = stack.pop()
            for neigh in graph[node]:
                if neigh in visited:
                    continue
                visited.add(neigh)
                stack.append(neigh)

        
    def recursiveDfs(self,):
        pass


    def hasCycle(node, parent, graph, visited):
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor == parent:
                continue
            if neighbor in visited:
                return False
            if not self.dfs(neighbor, node, graph, visited):
                return False
        return True