from collections import deque

class Solution:
    # Time: O(V+E)
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph, indegree = self.buildGraph(numCourses, prerequisites)
        queue = self.initializeQueue(numCourses, indegree)
        completedCourses = self.processQueue(graph, indegree, queue)
        return completedCourses == numCourses

    def buildGraph(self,numCourses:int, prerequisites: List[List[int]]):
        graph = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses
        for course, prerequisite in prerequisites:
            graph[prerequisite].append(course)
            indegree[course] += 1
        return graph, indegree

    def initializeQueue(self,numCourses:int, indegree:List[int]):
        queue = deque()
        for course in range(numCourses):
            if indegree[course] == 0:
                queue.append(course)
        return queue

    def processQueue(self, graph, indegree, queue):
        completedCourses = 0
        while queue:
            course = queue.popleft()
            completedCourses += 1
            for nextcourse in graph[course]:
                indegree[nextcourse] -= 1
                if indegree[nextcourse] == 0:
                    queue.append(nextcourse)
        return completedCourses
        