from collections import deque , defaultdict
class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """

        graph = defaultdict(list)
        indeg = [0] * numCourses 

        for a , b in prerequisites:
            graph[b].append(a)
            indeg[a] += 1

        q = deque( i for i in range(numCourses ) if indeg[i] == 0 ) 

        taken = 0 

        while q :
            u  = q.popleft()
            taken += 1 
            for v in graph[u]:
                indeg[v] -= 1
                if indeg[v] == 0:
                    q.append(v)

        return taken == numCourses
    
