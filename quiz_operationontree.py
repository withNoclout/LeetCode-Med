class LockingTree(object):

    def __init__(self, parent):
        """
        :type parent: List[int]
        """
        self.parent = parent
        n = len(parent)
        self.children = [[] for _ in range(n)]
        for i in range(1, n):
            self.children[parent[i]].append(i)
        self.locked_by = [-1] * n  # -1 means unlocked

    def lock(self, num, user):
        """
        :type num: int
        :type user: int
        :rtype: bool
        """
        if self.locked_by[num] != -1:
            return False
        self.locked_by[num] = user
        return True

    def unlock(self, num, user):
        """
        :type num: int
        :type user: int
        :rtype: bool
        """
        if self.locked_by[num] != user:
            return False
        self.locked_by[num] = -1
        return True

    def upgrade(self, num, user):
        """
        :type num: int
        :type user: int
        :rtype: bool
        """
        # Rule 1: node must be unlocked
        if self.locked_by[num] != -1:
            return False

        # Rule 2: none of the ancestors is locked
        p = self.parent[num]
        while p != -1:
            if self.locked_by[p] != -1:
                return False
            p = self.parent[p]

        # Rule 3: at least one locked descendant; unlock all locked descendants
        found_locked = False
        stack = list(self.children[num])
        to_unlock = []
        while stack:
            v = stack.pop()
            if self.locked_by[v] != -1:
                found_locked = True
                to_unlock.append(v)
            stack.extend(self.children[v])

        if not found_locked:
            return False

        for v in to_unlock:
            self.locked_by[v] = -1

        self.locked_by[num] = user
        return True
