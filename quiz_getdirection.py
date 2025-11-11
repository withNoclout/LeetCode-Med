class Solution(object):
    def getDirections(self, root, startValue, destValue):
        def dfs(node, target, path):
            if not node:
                return False
            if node.val == target:
                return True
            path.append('L')
            if dfs(node.left, target, path):
                return True
            path.pop()
            path.append('R')
            if dfs(node.right, target, path):
                return True
            path.pop()
            return False

        pathS, pathD = [], []
        dfs(root, startValue, pathS)
        dfs(root, destValue, pathD)

        i = 0
        while i < len(pathS) and i < len(pathD) and pathS[i] == pathD[i]:
            i += 1

        return 'U' * (len(pathS) - i) + ''.join(pathD[i:])
