from collections import deque
class Solution(object):
    def updateMatrix(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[List[int]]
        """
        m ,n = len(mat), len(mat[0])    
        q =deque()

        dist = [[-1] * n for _ in range(m) ] 

        for i in range(m) :
            for j in range(n) :
                if mat[i][j] == 0 :
                    dist[i][j] = 0
                    q.append((i,j))

        directions = [(0,1), (1,0), (0,-1), (-1,0)  ]

        while q : 
            i , j = q.popleft()
            for di , dj  in directions : 
                ni , nj = i + di , j + dj
                if 0 <= ni < m and 0 <= nj < n and dist[ni][nj] == -1 :
                    dist[ni][nj] = dist[i][j] + 1
                    q.append((ni,nj))
        return dist 
    
