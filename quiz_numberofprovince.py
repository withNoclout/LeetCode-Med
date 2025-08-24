class Solution(object):
    def findCircleNum(self, isConnected):
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """
        n = len(isConnected ) 
        visited = [False ] * n 

        def dfs(i ) :
            for j in range(n) :
                if isConnected[i][j] == 1 and not visited[j] :
                    visited[j] = True 
                    dfs(j) 

        province = 0  
        for i in range(n) :
            if not visited[i] : 
                province += 1 
                visited[i] = True 
                dfs(i) 


        return province
