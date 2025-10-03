class Solution(object):
    def checkIfPrerequisite(self, numCourses, prerequisites, queries):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :type queries: List[List[int]]
        :rtype: List[bool]
        """
        reach = [[False] * numCourses for _ in range(numCourses)]
        for u, v in prerequisites:
            reach[u][v] = True

        # Floyd-Warshall style transitive closure
        for k in range(numCourses):
            for i in range(numCourses):
                if reach[i][k]:
                    for j in range(numCourses):
                        if reach[k][j]:
                            reach[i][j] = True

        return [reach[u][v] for u, v in queries]
