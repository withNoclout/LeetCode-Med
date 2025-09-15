class Solution(object):
    def equationsPossible(self, equations):
        """
        :type equations: List[str]
        :rtype: bool
        """
        parent = {}

        def find(x):
            if x != parent.setdefault(x, x):
                parent[x] = find(parent[x])
            return parent[x]

        # Union for '=='
        for eq in equations:
            if eq[1:3] == '==':
                parent[find(eq[0])] = find(eq[3])

        # Check for '!='
        for eq in equations:
            if eq[1:3] == '!=' and find(eq[0]) == find(eq[3]):
                return False
        return True
