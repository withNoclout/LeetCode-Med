class Solution(object):
    def getFolderNames(self, names):
        """
        :type names: List[str]
        :rtype: List[str]
        """
        used = {}
        res = []

        for name in names:
            if name not in used:
                used[name] = 1
                res.append(name)
            else:
                k = used[name]
                while name + "(" + str(k) + ")" in used:
                    k += 1
                new_name = name + "(" + str(k) + ")"
                used[name] = k + 1
                used[new_name] = 1
                res.append(new_name)
        return res
