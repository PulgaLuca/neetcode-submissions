from typing import List, Tuple

class Solution:

    def findCheapestPrice(
        self,
        n: int,
        flights: List[List[int]],
        src: int,
        dst: int,
        k: int
    ) -> int:

        distances = self.initializeDistances(n, src)

        for _ in range(k + 1):

            distances, updated = self.relaxFlights(distances, flights)

            if not updated:
                break

        if distances[dst] == float('inf'):
            return -1

        return int(distances[dst])


    def initializeDistances(
        self,
        n: int,
        src: int
    ) -> List[float]:

        distances = [float('inf')] * n
        distances[src] = 0

        return distances


    def relaxFlights(
        self,
        distances: List[float],
        flights: List[List[int]]
    ) -> Tuple[List[float], bool]:

        nextDistances = distances.copy()
        updated = False

        for source, target, price in flights:

            if distances[source] == float('inf'):
                continue

            newPrice = distances[source] + price

            if newPrice >= nextDistances[target]:
                continue

            nextDistances[target] = newPrice
            updated = True

        return nextDistances, updated
