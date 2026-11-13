
from collections import deque
from typing import List, Deque, Tuple


class Solution:

    def findOrder(
        self,
        numCourses: int,
        prerequisites: List[List[int]]
    ) -> List[int]:

        graph, indegree = self.buildGraph(numCourses, prerequisites)

        queue = self.initializeQueue(indegree, numCourses)

        order = self.processCourses(graph, indegree, queue)

        if len(order) != numCourses:
            return []

        return order


    def buildGraph(
        self,
        numCourses: int,
        prerequisites: List[List[int]]
    ) -> Tuple[List[List[int]], List[int]]:

        graph = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses

        for course, prerequisite in prerequisites:
            graph[prerequisite].append(course)
            indegree[course] += 1

        return graph, indegree


    def initializeQueue(
        self,
        indegree: List[int],
        numCourses: int
    ) -> Deque[int]:

        queue = deque()

        for course in range(numCourses):
            if indegree[course] == 0:
                queue.append(course)

        return queue


    def processCourses(
        self,
        graph: List[List[int]],
        indegree: List[int],
        queue: Deque[int]
    ) -> List[int]:

        order = []

        while queue:
            course = queue.popleft()
            order.append(course)

            for nextCourse in graph[course]:
                indegree[nextCourse] -= 1

                if indegree[nextCourse] == 0:
                    queue.append(nextCourse)

        return order
