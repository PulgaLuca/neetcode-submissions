import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = self.buildGraph(n, times)
        distances = self.dijkstra(graph, n, k)
        return self.getNetworkDelayTime(distances, n)

    
    def buildGraph(self, n, times):
        graph = [[] for _ in range(n+1)]
        for source, target, weight in times:
            graph[source].append((target, weight))
        return graph

    def dijkstra(self, graph, n, start):
        distances = [float('inf')] * (n+1)
        distances[start] = 0
        minHeap = [(0, start)]
        while minHeap:
            currTime, node = heapq.heappop(minHeap)
            if currTime > distances[node]:
                continue
            
            for neigh, weight in graph[node]:
                newTime = currTime + weight
                if newTime >= distances[neigh]:
                    continue
                distances[neigh] = newTime
                heapq.heappush(minHeap, (newTime, neigh))
        return distances
    
    def getNetworkDelayTime(self, distances, n):
        shortestTimes = distances[1:]
        # Verifica che tutti i nodi siano raggiungibili e restituisce il tempo massimo.
        if any(distance == float('inf') for distance in shortestTimes):
            return -1
        return int(max(shortestTimes))
