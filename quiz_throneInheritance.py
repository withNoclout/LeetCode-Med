class ThroneInheritance(object):

    def __init__(self, kingName):
        """
        :type kingName: str
        """
        self.king = kingName
        self.children = {kingName: []}
        self.dead = set()

    def birth(self, parentName, childName):
        """
        :type parentName: str
        :type childName: str
        :rtype: None
        """
        if parentName not in self.children:
            self.children[parentName] = []
        self.children[parentName].append(childName)
        self.children.setdefault(childName, [])

    def death(self, name):
        """
        :type name: str
        :rtype: None
        """
        self.dead.add(name)

    def getInheritanceOrder(self):
        """
        :rtype: List[str]
        """
        order = []

        def dfs(name):
            if name not in self.dead:
                order.append(name)
            for c in self.children.get(name, []):
                dfs(c)

        dfs(self.king)
        return order
o
