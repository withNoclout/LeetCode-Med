from collections import defaultdict , deque
class Solution(object):

    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        graph = defaultdict(list)
        indeg = [0] * numCourses

        for a , b in prerequisites:
            graph[b].append(a)
            indeg[a] += 1

        q = deque([ i for i in range(numCourses) if indeg[i] == 0 ] ) 
        order = []
        while  q : 
            u  = q.popleft()
            order.append(u) 
            for v in graph[u] :
                indeg[v] -= 1
                if indeg[v] == 0:
                    q.append(v)

        return order if len(order) == numCourses else []
